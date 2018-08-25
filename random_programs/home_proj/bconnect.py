#pi@raspberrypi:~ $ sudo bluetoothctl
#[NEW] Controller B8:27:EB:BA:47:CF raspberrypi [default]
#[NEW] Device C8:69:CD:5A:27:6F Apple TV
#[NEW] Device FC:58:FA:2B:E2:1F Philips BT50
#[NEW] Device 94:65:2D:74:74:B4 1hK6tVVjlfc6LO0aQ_60
#[Philips BT50]# exit
#[DEL] Controller B8:27:EB:BA:47:CF raspberrypi [default]pi@raspberrypi:~ $ sudo bluetoothctl
#[NEW] Controller B8:27:EB:BA:47:CF raspberrypi [default]
#[NEW] Device C8:69:CD:5A:27:6F Apple TV
#[NEW] Device FC:58:FA:2B:E2:1F Philips BT50
#[NEW] Device 94:65:2D:74:74:B4 1hK6tVVjlfc6LO0aQ_60
#[Philips BT50]# exit
#[DEL] Controller B8:27:EB:BA:47:CF raspberrypi [default]


# This program is to make sure Bluetooth Philips after every reboot. The script is loaded in cron with @reboot knob
import os
import time
import pexpect
child = pexpect.spawn("bluetoothctl")
child.expect('.*')
child.sendline("connect FC:58:FA:2B:E2:1F")
child.sendline("quit")
