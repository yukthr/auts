from hcsr04sensor import sensor
import time
import requests
value = sensor.Measurement(17, 27)


def sensor_reading():
    raw_distance = value.raw_distance()
    distance_cm = value.distance_metric(raw_distance)
    if distance_cm<35:
        cmd = "https://api.telegram.org/botxxx/sendMessage?chat_id=xxx&text='{} cms - Switch off Motor Now!'".format(distance_cm)
        requests.post(cmd)
    elif 36<distance_cm<69:
        cmd = "https://api.telegram.org/botxxx/sendMessage?chat_id=xxx&text='{} cms - Capacity More than Half'".format(distance_cm)
        requests.post(cmd)
    elif 70<distance_cm<100:
        cmd = "https://api.telegram.org/botxxx/sendMessage?chat_id=xxx&text='{} cms - Less than Half Tank Capcity Detected!'".format(distance_cm)
        requests.post(cmd)
    elif 101<distance_cm<130:
        cmd = "https://api.telegram.org/botxxx/sendMessage?chat_id=xxx&text='{} cms - Critically Low water capacity!'".format(distance_cm)
        requests.post(cmd)
    else:
        cmd = "https://api.telegram.org/botxxx/sendMessage?chat_id=xxx&text='{} cms - Low Water Level Detected'".format(distance_cm)
        requests.post(cmd)
    time.sleep(25)


while 1>0:
    try:
        sensor_reading()
    except:
        cmd = "https://api.telegram.org/botxxx/sendMessage?chat_id=xxx&text='Something went wrong - Check Manually'"
        requests.post(cmd)
