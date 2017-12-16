# Created by Luke Halley

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
            # Add values to their respective arrays
            print("Adding the following to the CarCount array", carCount)
            carAverage.append(carCount)
            print("Adding the following to the OtherCount array", otherCount)
            otherAverage.append(otherCount)
            # Resets the data for the next reason
            print("Resetting Data...")
            otherCount = 0
            carCount = 0
            print("Data Reset - Car:", carCount, "Other:", otherCount)
            count = count + 1
            print("Count: ", count)
            chrono.reset()
    else:
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
