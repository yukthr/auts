from pomodoro import pomodoro_timer
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    #wlan.ifconfig(('192.168.1.82','255.255.255.0','192.168.1.1','89.101.160.4'))
    if not wlan.isconnected():
        print('connecting to network...')
        try:
            wlan.connect('R-VMVMVM', 'Himaja@1992')
        except:
            pass
            #wlan.connect('R-VMVMVM','Himaja@1992')
    print('network config:', wlan.ifconfig())

do_connect()
pomodoro_timer()
