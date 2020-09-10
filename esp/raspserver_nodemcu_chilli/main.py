#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
import time
from machine import Pin,ADC
from time import sleep
import urequests
import json



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
    sensor_ping = machine.Pin(4,machine.Pin.OUT)
    sensor_ping.on()
    time.sleep(4)
    pot = ADC(0)
    moisture_detect['moisture_value'] = pot.read()
    sensor_ping.off()
    return moisture_detect


def post_to_raspberry_flask():
    print('entered function')
    payload = json.dumps(moisture_reading())
    print(payload)
    url = "http://192.168.0.150:5000/moisture"
    headers = {'Content-Type': "application/json"}
    response = urequests.request("POST", url, data=payload, headers=headers)
    print(response.text)


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

def sleep_hours():
    hourly_sleeper()
    machine.reset()

def whole_loop():
    try:
    	do_connect()
        post_to_raspberry_flask()
    except Exception as e:
        pass
    sleep(2)
    print("Entering DeepSleep")
    #deep_sleep(28800000)
    sleep_hours()

whole_loop()
