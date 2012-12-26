#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

import time
#import os

import click
import keyboard
import config
import autopy


def work():
    """
    使用说明：
    左边是小号，用chrome
    右边是大号，用IE
    都全屏。

    """
    time.sleep(3)
    click.click("searchbox")
    keyboard.type(config.roomid)
    time.sleep(1)
    click.click("searchbutton")
    time.sleep(1)
    click.click("searchbutton")
    time.sleep(1)
    click.click("enterroom")
    time.sleep(1)
    keyboard.type(config.passwd)
    time.sleep(1)
    click.click("enterbutton")

    time.sleep(1)
    click.click("ready")
    keyboard.switchUser("right")
    click.click("ready")

    keyboard.switchUser("left")
    time.sleep(2)
    click.click("trust")
    keyboard.switchUser("right")
    time.sleep(1)
    click.click("trust")

    time.sleep(15)
    click.click("trust")

    cnt = 10
    while cnt>0:
        cnt-=1
        time.sleep(5)
        click.click_till("yes", 1)
        click.click_till("no", 1)
        click.click_till("end", 1)
        click.click("card1")
        time.sleep(1)
        click.click("card2")
        time.sleep(1)
        click.click("card3")
        time.sleep(1)
        click.click_till("yes", 1)
        pass

    keyboard.switchUser("left")
    time.sleep(2)
    click.click("run")
    click.click("sure_run")
    time.sleep(1)
    keyboard.switchUser("right")
    time.sleep(1)
    click.click("sure")

    keyboard.switchUser("left")
    time.sleep(2)

if __name__ == "__main__":
    while True:
        work()
        time.sleep(3)