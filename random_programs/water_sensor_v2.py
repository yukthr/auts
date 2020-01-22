#!/usr/bin/python3


from influxdb import InfluxDBClient
import RPi.GPIO as GPIO
import os
import time




# Constants Definitions

client = InfluxDBClient(host='192.168.0.140', port=8086)
client.switch_database('water_measure')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 15
GPIO_ECHO = 14

TRIGGER_TIME = 0.00001
MAX_TIME = 0.004  # max time waiting for response in case something is missed
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Echo

GPIO.output(GPIO_TRIGGER, False)

class update_influx:

    def __init__(self, water_level):

        self.water_level = water_level

    def dynamic_json_update_influx(self):
        json_data = [
            {
                "measurement": "water_measure",
                "tags": {
                    "water_level" : "value",
                },
                "fields": {
                    "water_level" : "{}".format(self.water_level),
                }
            }
        ]

        client.write_points(json_data)


def measure():
    # Pulse the trigger/echo line to initiate a measurement
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(TRIGGER_TIME)
    GPIO.output(GPIO_TRIGGER, False)

    # ensure start time is set in case of very quick return
    start = time.time()
    timeout = start + MAX_TIME

    # set line to input to check for start of echo response
    while GPIO.input(GPIO_ECHO) == 0 and start <= timeout:
        start = time.time()

    if(start > timeout):
        return -1

    stop = time.time()
    timeout = stop + MAX_TIME
    # Wait for end of echo response
    while GPIO.input(GPIO_ECHO) == 1 and stop <= timeout:
        stop = time.time()

    if(stop <= timeout):
        elapsed = stop-start
        distance = float(elapsed * 34300)/2.0
    else:
        return -1
    return distance

def measure_and_publish():
    distance = measure()

    if(distance > -1):
        print("Measured Distance = %.1f cm" % distance)
        uf = update_influx(water_level=distance).dynamic_json_update_influx()
    else:
        print("#")
        time.sleep(0.5)

measure_and_publish()

