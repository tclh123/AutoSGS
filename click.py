#!/usr/bin/env python
__author__ = 'tclh123'

import autopy
import os
import time
import config

def click(button):
    time.sleep(0.2)
    point = config.point[button]
    autopy.mouse.move(point[0], 800-point[1])
    time.sleep(0.2)
    autopy.mouse.click()

def click_till(button, scs):
    scs*=2
    while scs>0:
        scs-=1
        time.sleep(0.2)
        point = config.point[button]
        autopy.mouse.move(point[0], 800-point[1])
        time.sleep(0.2)
        autopy.mouse.click()
        time.sleep(0.5)