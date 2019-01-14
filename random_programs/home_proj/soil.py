# water sensor

import time
import machine
import urequests

moisture_read = machine.Pin(5, machine.Pin.IN)
red_led = machine.Pin(12, machine.Pin.OUT)
green_led = machine.Pin(13, machine.Pin.OUT)

def soil():
    while True:
        red_led.on()
        green_led.on()
        moisture = moisture_read.value()
        print(moisture)
        time.sleep(10)
        if moisture == 1:
            red_led.off()
	    time.sleep(5)
            red_led.on()
            try:
                urequests.post('https://dweet.io/dweet/for/rakesh1189727?moisture=0',data='')
            except:
                continue
        if moisture == 0:
            green_led.on()
            time.sleep(5)
            green_led.off()
            try:
                urequests.post('https://dweet.io/dweet/for/rakesh1189727?moisture=1',data='')
            except:
                continue
