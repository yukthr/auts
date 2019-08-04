from machine import Pin, I2C
import ssd1306
import time
from writer import Writer
import courier
import machine
import urequests

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))


def post_to_slack(message):
    url = "Ur Slack URL"

    payload = "{\"text\":\"" + message + "\"}"
    headers = {
        'Content-type': "application/json",
    }
    response = urequests.request("POST", url, data=payload, headers=headers)


def pomodoro_timer():
    for j in range(6):
        if j < 5:
            for i in range(25):
                oled_width = 128
                oled_height = 64
                oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
                wri = Writer(oled, courier, verbose=False)
                Writer.set_textpos(oled, 14, 0)  # In case a previous test has altered this
                wri.printstring('{} Mins '.format(25 - i))
                wri.printstring('\n{}/5 Iters'.format(j+1))
                oled.show()
                time.sleep(60)
            for k in range(5):
                oled_width = 128
                oled_height = 64
                oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
                wri = Writer(oled, courier, verbose=False)
                Writer.set_textpos(oled, 14, 0)  # In case a previous test has altered this
                wri.printstring('{} Break '.format(5 - k))
                oled.show()
                if k == 0:
                    post_to_slack("5M Break")
                time.sleep(60)
        else:
            for l in range(15):
                if l == 0:
                    post_to_slack("15M Break!")
                oled_width = 128
                oled_height = 64
                oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
                wri = Writer(oled, courier, verbose=False)
                Writer.set_textpos(oled, 14, 0)  # In case a previous test has altered this
                wri.printstring('{} Break '.format(15 - l))
                oled.show()
                time.sleep(60)
    machine.reset()
