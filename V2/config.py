#!/usr/bin/env python
__author__ = 'tclh123'

dir_img = "Resource/image/"
button_img = {
    "searchbox":"room_search_box.png",
    "searchbutton":"search_button.png",
    "test":"test.png"
}

def filename(button):
    return dir_img+button_img[button]