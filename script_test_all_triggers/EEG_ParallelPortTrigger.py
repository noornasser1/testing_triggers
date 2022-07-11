#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
parallel ports demo

This is for win32 only.
"""

from __future__ import absolute_import, division, print_function

from builtins import range
from psychopy import visual, core
from psychopy import parallel

def parallel_init():
    parallel.setPortAddress((0x5EFC))  # address for parallel port on many machines

def eeg():
    parallel.setData(0)
    parallel.setPin(2, 1)  # sets pin (2) to be high (1)




