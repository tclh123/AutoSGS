#!/usr/bin/env python
__author__ = 'tclh123'

# import autopy
# def hello_there_world():
#     autopy.alert.alert("Hello, world")
# hello_there_world()

import autopy
import math
import time
import random
import os

# TWO_PI = math.pi * 2.0
# def sine_mouse_wave():
#     """
#     Moves the mouse in a sine wave from the left edge of
#     the screen to the right.
#     """
#     width, height = autopy.screen.get_size()
#     height /= 2
#     height -= 10 # Stay in the screen bounds.

#     for x in xrange(width):
#         y = int(height * math.sin((TWO_PI * x) / width) + height)
#         autopy.mouse.move(x, y)
#         time.sleep(random.uniform(0.001, 0.003))

# sine_mouse_wave()

#time.sleep(1)
#os.system("screencapture -x -r foo.png")

#time.sleep(1)
#os.system("screencapture -x -r -R100,100,200,200 foo2.png") # ??
#os.system("screencapture -x -r -R410,50,18,18 foo2.png")

bmp = autopy.bitmap.Bitmap.open("foo.png")
time.sleep(1)
bmp2 = autopy.bitmap.Bitmap.open("foo2.png")
time.sleep(1)
ret = bmp.find_bitmap(bmp2)

autopy.alert.alert(str(ret))

#point = ret
#autopy.mouse.move(point[0]+5, point[1]+5)
## time.sleep(1)
#autopy.mouse.click()