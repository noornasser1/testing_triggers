from psychopy import core
from pylsl import StreamInfo, StreamOutlet

def lsl_init():
    info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
    # next make an outlet
    outlet = StreamOutlet(info)
    return outlet

def lsl(outlet):
    outlet.push_sample(["hello"])
