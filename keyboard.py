#!/usr/bin/env python
__author__ = 'tclh123'

import autopy
import time

def type(str):
    time.sleep(0.2)
    autopy.key.type_string(str,30)

def switchUser(dir):
    time.sleep(1)
    if dir == "left":
        autopy.key.toggle(autopy.key.K_LEFT, True, autopy.key.MOD_CONTROL)
        time.sleep(0.2)
        autopy.key.toggle(autopy.key.K_LEFT, False, autopy.key.MOD_CONTROL)
        time.sleep(2)
        autopy.key.tap(autopy.key.MOD_CONTROL)
    else:
        autopy.key.toggle(autopy.key.K_RIGHT, True, autopy.key.MOD_CONTROL)
        time.sleep(0.2)
        autopy.key.toggle(autopy.key.K_RIGHT, False, autopy.key.MOD_CONTROL)
    time.sleep(1)