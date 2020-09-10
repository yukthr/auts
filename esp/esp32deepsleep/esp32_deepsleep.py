import time
import machine
from machine import Pin,ADC
from time import sleep
import urequests
import json



# Deep Sleep function

def deep_sleep(msecs):
  #configure RTC.ALARM0 to be able to wake the device
  machine.deepsleep(msecs)


#Function to extract moisture value

def moisture_reading():
    moisture_detect = {}
    sensor_ping = Pin(18, Pin.OUT)
    sensor_ping.on()
    time.sleep(4)
    pot = ADC(Pin(34))
    pot.atten(ADC.ATTN_11DB)
    moisture_detect['flower_pot_front1'] = pot.read()
    sensor_ping.off()
    return moisture_detect


def post_to_raspberry_flask():
    print('entered function')
    payload = json.dumps(moisture_reading())
    print(payload)
    url = "http://192.168.0.151:5000/moisture"
    headers = {'Content-Type': "application/json"}
    response = urequests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('R-VMVMVM', 'a')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def whole_loop():
    try:
        do_connect()
        post_to_raspberry_flask()
    except Exception as e:
        pass
    sleep(2)
    print("Entering DeepSleep")
    deep_sleep(21600000)

whole_loop()

