from threading import Thread, Event
import os
import json
import numpy as np
import awscam
import cv2
import greengrasssdk
import time
import base64
import urllib
import zipfile
import sys
import datetime

import boto3

bucket_name = "deeplenss3bucket"

client = greengrasssdk.client('iot-data')
iot_topic = '$aws/things/{}/infer'.format(os.environ['AWS_IOT_THING_NAME'])

class LocalDisplay(Thread):
    """ Class for facilitating the local display of inference results
        (as images). The class is designed to run on its own thread. In
        particular the class dumps the inference results into a FIFO
        located in the tmp directory (which lambda has access to). The
        results can be rendered using mplayer by typing:
        mplayer -demuxer lavf -lavfdopts format=mjpeg:probesize=32 /tmp/results.mjpeg
    """
    def __init__(self, resolution):
        """ resolution - Desired resolution of the project stream """
        # Initialize the base class, so that the object can run on its own
        # thread.
        super(LocalDisplay, self).__init__()
        # List of valid resolutions
        RESOLUTION = {'1080p' : (1920, 1080), '720p' : (1280, 720), '480p' : (858, 480)}
        if resolution not in RESOLUTION:
            raise Exception("Invalid resolution")
        self.resolution = RESOLUTION[resolution]
        # Initialize the default image to be a white canvas. Clients
        # will update the image when ready.
        self.frame = cv2.imencode('.jpg', 255*np.ones([640, 480, 3]))[1]
        self.stop_request = Event()

    def run(self):
        """ Overridden method that continually dumps images to the desired
            FIFO file.
        """
        result_path = '/tmp/results.mjpeg'
        if not os.path.exists(result_path):
            os.mkfifo(result_path)
        with open(result_path, 'w') as fifo_file:
            while not self.stop_request.isSet():
                try:
                    fifo_file.write(self.frame.tobytes())
                except IOError:
                    continue

    def set_frame_data(self, frame):
        ret, jpeg = cv2.imencode('.jpg', cv2.resize(frame, self.resolution))
        if not ret:
            raise Exception('Failed to set frame data')
        self.frame = jpeg

    def join(self):
        self.stop_request.set()

def push_to_s3(img):
    try:
        index = 0

        timestamp = int(time.time())
        now = datetime.datetime.now()
        key = "dog_{}_{}_{}_{}_{}_{}.jpg".format(now.month, now.day,
                                                   now.hour, now.minute,
                                                   timestamp, index)

        s3 = boto3.client('s3')

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        _, jpg_data = cv2.imencode('.jpg', img, encode_param)
        response = s3.put_object(ACL='private',
                                 Body=jpg_data.tostring(),
                                 Bucket=bucket_name,
                                 Key=key)

        client.publish(topic=iot_topic, payload="Response: {}".format(response))
        client.publish(topic=iot_topic, payload="Frame pushed to S3")
    except Exception as e:
        msg = "Pushing to S3 failed: " + str(e)
        client.publish(topic=iot_topic, payload=msg)


def greengrass_infinite_infer_run():
    """ Entry point of the lambda function"""
    try:
    model_type = 'ssd'
        output_map = {1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat', 5: 'bottle', 6: 'bus',
                      7 : 'car', 8 : 'cat', 9 : 'chair', 10 : 'cow', 11 : 'dinning table',
                      12 : 'dog', 13 : 'horse', 14 : 'motorbike', 15 : 'person',
                      16 : 'pottedplant', 17 : 'sheep', 18 : 'sofa', 19 : 'train',
                      20 : 'tvmonitor'}

        local_display = LocalDisplay('480p')
        local_display.start()
        model_path = '/opt/awscam/artifacts/mxnet_deploy_ssd_resnet50_300_FP16_FUSED.xml'
        client.publish(topic=iot_topic, payload='Loading object detection model')
        model = awscam.Model(model_path, {'GPU': 1})
        client.publish(topic=iot_topic, payload='Object detection model loaded')
        detection_threshold = 0.25
        input_height = 300
        input_width = 300
        while True:
            detectedDog = False
            ret, frame = awscam.getLastFrame()
            if not ret:
                raise Exception('Failed to get frame from the stream')
            frame_resize = cv2.resize(frame, (input_height, input_width))
            parsed_inference_results = model.parseResult(model_type,
            yscale = float(frame.shape[0]/input_height)
            xscale = float(frame.shape[1]/input_width)
            cloud_output = {}
            detectedDog = False
            for obj in parsed_inference_results[model_type]:
                if obj['prob'] > detection_threshold:
                    if(output_map[obj['label']] == 'dog'):
                        detectedDog = True
                        break

            if(detectedDog):
                rfr = cv2.resize(frame, (672, 380))
                push_to_s3(rfr)
                time.sleep(30)

            for obj in parsed_inference_results[model_type]:
                if obj['prob'] > detection_threshold:

                    if(output_map[obj['label']] == 'dog'):
                        detectedDog = True

                    # Add bounding boxes to full resolution frame
                    xmin = int(xscale * obj['xmin']) \
                           + int((obj['xmin'] - input_width/2) + input_width/2)
                    ymin = int(yscale * obj['ymin'])
                    xmax = int(xscale * obj['xmax']) \
                           + int((obj['xmax'] - input_width/2) + input_width/2)
                    ymax = int(yscale * obj['ymax'])
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 165, 20), 10)
                    text_offset = 15
                    cv2.putText(frame, "{}: {:.2f}%".format(output_map[obj['label']],
                                                               obj['prob'] * 100),
                                (xmin, ymin-text_offset),
                                cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 165, 20), 6)
                    cloud_output[output_map[obj['label']]] = obj['prob']
            local_display.set_frame_data(frame)
            client.publish(topic=iot_topic, payload=json.dumps(cloud_output))
    except Exception as ex:
        client.publish(topic=iot_topic, payload='Error in object detection lambda: {}'.format(ex))

greengrass_infinite_infer_run()

