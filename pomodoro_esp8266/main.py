
import time
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        try:
            wlan.connect('R-VMVMVM', '')
            if '0.0.0.0' in wlan.ifconfig():
                wlan.connect('R-VMVMVM', '')
        except: 
            wlan.connect('R-VMVMVM','')
    print('network config:', wlan.ifconfig())

do_connect()
import pomodoro
