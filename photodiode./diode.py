# Testing all 3 triggers
from psychopy import core, visual
from psychopy import core
from pylsl import StreamInfo, StreamOutlet
from builtins import range
import serial

win = visual.Window(
    [800, 600], fullscr = True, monitor="testMonitor", units="deg", color=(-1, -1, -1), useFBO=False
    )

options = ["black.jpg","white.jpg"]
black= visual.ImageStim(win, image="black.jpg",  units='norm', size=[2,2], interpolate = True)
white = visual.ImageStim(win, image="white.jpg",  units='norm', size=[2,2], interpolate = True)
info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

core.wait(15)

def main(win):
    for i in range(100):
        black.draw()
        win.update()
        core.wait(1)
        white.draw()
        win.update()
        outlet.push_sample(["hello"])
        core.wait(1)   
    win.close()

main(win)