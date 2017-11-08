# Imports
import machine
import socket
import sys
import gc
import pycom
from network import Sigfox
from machine import Timer
from machine import Pin

# ------------------ SFX SETUP ------------------
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
# make the socket blocking
s.setblocking(True)
# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# ------------------ LED SETUP ------------------
# Disables heartbeat to enable the LED to be used
pycom.heartbeat(False)
# // Extremely accurate timer
chrono = Timer.Chrono()
# Sets the time distinguished between a short and long press
timer = Timer.Alarm(None, 1, periodic = False)
# Turn Pull-up ON to dectect button pressing
btn = Pin(Pin.exp_board.G17, mode=  Pin.IN, pull=Pin.PULL_UP)

# ------------------ BTN SETUP ------------------
shortPress = 0
longPress = 0

# ------------------ TMR SETUP ------------------
class Clock:

    def __init__(self):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, 30, periodic=True)

    def _seconds_handler(self, alarm):
        self.seconds += 30
        print("%02d seconds have passed" % self.seconds)
        print("SENDING DATA...")
        pycom.rgbled(0x7f0000) # red
        s.send(longPress)
        pycom.rgbled(0x007f00) # green
        # TODO Fix sigfox message sending, cant send int value up

clock = Clock()

def long_press_handler(alarm):
    global longPress
    longPress += 1
    pycom.rgbled(0x1DDCDC) # color
    print(longPress)

def single_press_handler():
    global shortPress
    shortPress += 1
    pycom.rgbled(0xB31DDC) # green
    print(shortPress)

def btn_press_detected(arg):
    global chrono,  timer
    try:
        val = btn()
        if 0 == val:
            chrono.reset()
            chrono.start()
            timer.callback(long_press_handler)
        else:
            timer.callback(None)
            chrono.stop()
            t = chrono.read_ms()
            if (t > 30) & (t < 200):
                single_press_handler()
    finally:
        gc.collect()

btn.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING,  btn_press_detected)
