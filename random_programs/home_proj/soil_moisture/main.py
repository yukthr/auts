def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('R-VM', 'Himaja@1992')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()

import led_blink
import soil
soil.soil()
led_blink.led_blink()
