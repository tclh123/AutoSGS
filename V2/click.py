#!/usr/bin/env python
__author__ = 'tclh123'

import autopy
import os
import time
import config

def click(button):
#    os.system("screencapture -x -r screen.png")
#    time.sleep(5)
#    os.system("screencapture -x -r -R410,50,428,69 foo2.png")
    screen = autopy.bitmap.Bitmap.open("screen.png")
    time.sleep(1)
    pattern = autopy.bitmap.Bitmap.open(config.filename(button))
    time.sleep(1)
    point = screen.find_bitmap(pattern)
    autopy.mouse.move(point[0]+5, point[1]+5)
    # time.sleep(1)
    autopy.mouse.click()