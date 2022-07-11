# Testing all 3 triggers
from psychopy import core, visual
from pylsl import StreamInfo, StreamOutlet
from builtins import range
from psychopy import parallel
import serial
import random

#initilize triggers and stream
parallel.setPortAddress((0x5EFC))  # address for parallel port on many machines
info   = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)
ser    = serial.Serial("COM4", 1200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=False)

def eeg():
    parallel.setData(0)
    parallel.setPin(2, 1)  # sets pin (2) to be high (1)

def et():
    if ser.isOpen():
        ser.close()
    ser.open()
    ser.setRTS(False)
    ser.close()

core.wait(15) #this is a temporary solution.

#main loop
def main():
    for i in range(100):
        #send three triggers (eeg, lsl, eyetracker)
        outlet.push_sample(["hello"])
        eeg()
        et()
        #core.wait(random.sample([0.5,1.5],1)[0]) testing with jitter
        core.wait(1)      
    print("done")
main()
