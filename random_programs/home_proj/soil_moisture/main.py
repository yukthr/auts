#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
from umqtt.robust import MQTTClient
import time
from machine import Pin,ADC
from time import sleep
import json

#This works for either ESP8266 ESP32 if you rename certs before moving into /flash
CERT_FILE = "cert"
KEY_FILE = "key"

#if you change the ClientId make sure update AWS policy
MQTT_CLIENT_ID = "basicPubSub"
MQTT_PORT = 8883

#if you change the topic make sure update AWS policy
MQTT_TOPIC = "xxxxx"

#Change the following three settings to match your environment
MQTT_HOST = "xxxx-ats.iot.eu-west-1.amazonaws.com"

mqtt_client = None

# Deep Sleep function

def deep_sleep(msecs):
  #configure RTC.ALARM0 to be able to wake the device
  rtc = machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
  # set RTC.ALARM0 to fire after Xmilliseconds, waking the device
  rtc.alarm(rtc.ALARM0, msecs)
  #put the device to sleep
  machine.deepsleep()





#Function to extract moisture value

def moisture_reading():
    moisture_detect = {}
    pot = ADC(0)
    moisture_detect['moisture_value'] = pot.read()
    return moisture_detect

def pub_msg(msg):
    global mqtt_client
    try:
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

def connect_mqtt():
    global mqtt_client

    try:
        with open(KEY_FILE, "r") as f:
            key = f.read()

        print("Got Key")

        with open(CERT_FILE, "r") as f:
            cert = f.read()

        print("Got Cert")

        mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000, ssl=True, ssl_params={"cert":cert, "key":key, "server_side":False})
        mqtt_client.connect()
        print('MQTT Connected')


    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('R-VMVMVM', 'xxxxx')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def whole_loop():
    try:
    	do_connect()
        connect_mqtt()
        pub_msg("{}".format(json.dumps(moisture_reading())))
    except Exception as e:
        print(str(e))
    sleep(200)
    print("Entering DeepSleep")
    deep_sleep(3600000)

while True:
    whole_loop()
