# Imports
import machine
import socket
import sys
import gc
import pycom
from network import Sigfox
from machine import Timer
from machine import Pin
from struct import *
import struct

# TODO: Create callback for messages that didnt make it :(
# TODO: Graph out data with service
# TODO: Report/Docs
# https://api.mlab.com/api/1//databases/carpass/collections/WITCarpark?apiKey=tadpKQNZ0ssAbZJ_-4PC3_1zOYpq0b3R

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
# Sets the time distinguished between a Other and Car press
timer = Timer.Alarm(None, 1, periodic = False)
# Turn Pull-up ON to dectect button pressing
btn = Pin(Pin.exp_board.G17, mode=  Pin.IN, pull=Pin.PULL_UP)

# ------------------ BTN SETUP ------------------
otherCount = 0
carCount = 0

# ------------------ TMR SETUP ------------------
class Clock:

    def __init__(self):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, 30, periodic=True)

    def _seconds_handler(self, alarm):
        global carCount
        global otherCount
        self.seconds += 30
        print("%02d seconds have passed" % self.seconds)
        print("Sending Data - Car:", carCount, "Other:", otherCount)
        pycom.rgbled(0x7f0000) # red
        longByteArray = bytearray(struct.pack("h", carCount))
        longByteArray.extend(bytearray(struct.pack("h", otherCount)))
        s.send(longByteArray)
        pycom.rgbled(0x007f00) # green
        print("DATA HAS BEEN SENT!")
        print("Resetting Data...")
        otherCount = 0
        carCount = 0
        print("Data Reset - Car:", carCount, "Other:", otherCount)

clock = Clock()

def long_press_handler(alarm):
    global carCount
    carCount += 1
    pycom.rgbled(0x1DDCDC) # color
    print(carCount)

def single_press_handler():
    global otherCount
    otherCount += 1
    pycom.rgbled(0xB31DDC) # green
    print(otherCount)

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
