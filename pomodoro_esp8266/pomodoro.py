from machine import Pin, I2C
import ssd1306
import time
from writer import Writer
import courier
import machine
import urequests

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))


def  post_to_slack(message):
  

    url = "your slack url here"

    payload = "{\"text\":\""+message+"\"}"
    headers = {
        'Content-type': "application/json",
    }
    response = urequests.request("POST", url, data=payload, headers=headers)


def pomodoro_timer():
    for j in range(5):
        if j <=5:
            for i in range(25):
                if i <=25:
                    oled_width = 128
                    oled_height = 64
                    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
                    wri = Writer(oled, courier, verbose=False)
                    Writer.set_textpos(oled, 14, 0) # In case a previous test has altered this
                    wri.printstring('{} Mins '.format(25-i))
                    wri.printstring('\n{}/5 Iters'.format(j))
                    oled.show()
                    time.sleep(60)
                    i = i + 1
                else:
                    for k in range(5):
                        if k <= 5:
                            post_to_slack("5m Break")
                            oled_width = 128
                            oled_height = 64
                            oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
                            wri = Writer(oled, courier, verbose=False)
                            Writer.set_textpos(oled, 14, 0)  # In case a previous test has altered this
                            wri.printstring('{} Break '.format(5 - k))
                            oled.show()
                            time.sleep(60)
                            k = k + 1
                            post_to_slack("25M  start")

            j=j+1

        else:
            for l in range(15):
                if l <= 15:
                    post_to_slack("15m Break start")
                    oled_width = 128
                    oled_height = 64
                    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
                    wri = Writer(oled, courier, verbose=False)
                    Writer.set_textpos(oled, 14, 0)  # In case a previous test has altered this
                    wri.printstring('{} 15 Break '.format(15 - l))
                    oled.show()
                    time.sleep(60)
                    l = l + 1

pomodoro_timer()
machine.reset()
