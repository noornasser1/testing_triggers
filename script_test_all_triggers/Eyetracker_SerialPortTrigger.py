from __future__ import absolute_import, division, print_function
from psychopy import core, visual
import pylsl as lsl
from builtins import range
from psychopy import parallel
import serial
import time

##Initializing game

# # create a window
def ser_init():    
    ser = serial.Serial("COM4", 1200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=False)
    return ser
# Experiment Flow Function    
def et(ser):
    if ser.isOpen():
        ser.close()
    ser.open()
    ser.setRTS(False)
    ser.close()
