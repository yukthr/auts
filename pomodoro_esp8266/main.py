from pomodoro import pomodoro_timer
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        try:
            wlan.connect('R-VMVMVM', 'xxxx')
        except:
            pass
    print('network config:', wlan.ifconfig())

do_connect()
pomodoro_timer()
