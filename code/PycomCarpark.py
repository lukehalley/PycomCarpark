# TODO Get average car count for say 10 minutes taking a reading in every minute
# TODO Get that average to send up to sigfox

# Imports
import machine
import socket
import sys
import gc
import pycom
import time
import array
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
chrono2 = Timer.Chrono()
# Sets the time distinguished between a Other and Car press
timer = Timer.Alarm(None, 1, periodic = False)
# Turn Pull-up ON to dectect button pressing
btn = Pin(Pin.exp_board.G17, mode=  Pin.IN, pull=Pin.PULL_UP)

# ------------------ BTN SETUP ------------------
otherCount = 0
carCount = 0

# ------------------ TMR SETUP ------------------
# class Clock:

    # def __init__(self):
    #     self.seconds = 0
    #     self.__alarm = Timer.Alarm(self._seconds_handler, 60, periodic=True)
        # class Timer.Alarm(handler=None, s, * , ms, us, arg=None, periodic=False)

    # def _seconds_handler(self, alarm):
    #     global carCount
    #     global otherCount
    #     self.seconds += 30
    #     print("%02d seconds have passed" % self.seconds)
    #     print("Sending Data - Car:", carCount, "Other:", otherCount)
    #     pycom.rgbled(0x7f0000) # red
    #     longByteArray = bytearray(struct.pack("h", carCount))
    #     longByteArray.extend(bytearray(struct.pack("h", otherCount)))
    #     # s.send(longByteArray)
    #     pycom.rgbled(0x007f00) # green
    #     print("DATA HAS BEEN SENT!")
    #     print("Resetting Data...")
    #     otherCount = 0
    #     carCount = 0
    #     print("Data Reset - Car:", carCount, "Other:", otherCount)

def messageTime():
    global carCount
    global otherCount
    count = 0
    carAverage = []
    otherAverage = []
    # Start the timer
    chrono.start()
    # While the count is less than an hour
    while count < 3:
        # Every 10 minutes a value is taken in, the time is printed until then
        while chrono.read() < 20:
            print(chrono.read())
        else:
            # Add values to an array
            print("Adding the following to the CarCount array", carCount)
            carAverage.append(carCount)
            print("Adding the following to the OtherCount array", otherCount)
            otherAverage.append(otherCount)
            print("Resetting Data...")
            otherCount = 0
            carCount = 0
            print("Data Reset - Car:", carCount, "Other:", otherCount)
            count = count + 1
            print("Count: ", count)
            time.sleep(5)
            chrono.reset()
    else:
        print("AVRG DATA")
        print(carAverage)
        print(otherAverage)
        time.sleep(20)
        carCountAverage = int(sum(carAverage)/len(carAverage))
        otherCountAverage = int(sum(otherAverage)/len(otherAverage))
        print("Average Data - Cars:", carCountAverage, "Others:", otherCountAverage)
        print("SENDING DATA")
        pycom.rgbled(0x7f0000) # red
        longByteArray = bytearray(struct.pack("h", carCountAverage))
        longByteArray.extend(bytearray(struct.pack("h", otherCountAverage)))
        print("Sending The Following Data - Cars:", carCountAverage, "Others:", otherCountAverage)
        s.send(longByteArray)
        print("DATA SENT!")

def long_press_handler(alarm):
    global carCount
    carCount += 1
    pycom.rgbled(0x1DDCDC) # blue
    print(carCount)

def single_press_handler():
    global otherCount
    otherCount += 1
    pycom.rgbled(0xB31DDC) # green
    print(otherCount)

def btn_press_detected(arg):
    global chrono2, timer
    try:
        val = btn()
        if 0 == val:
            chrono2.reset()
            chrono2.start()
            timer.callback(long_press_handler)
        else:
            timer.callback(None)
            chrono2.stop()
            t = chrono2.read_ms()
            if (t > 30) & (t < 200):
                single_press_handler()
    finally:
        gc.collect()

while True:
    btn.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING,  btn_press_detected)
    messageTime()
