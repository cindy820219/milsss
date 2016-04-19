import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

import for_sheet
import for_modify
import for_metronome

import time


def red_line(Tem):
    print('aaaaa')
    # create the canvas, size in pixels
    canvas = Canvas(width = 700, height = 200, bg = 'yellow')
    # pack the canvas into a frame/form
    canvas.place(x= 200 ,y=20)
    # load the .gif image file
    # put in your own gif file here, may need to add full path
    # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
    gif1 = PhotoImage(file = 'red_line.gif')
    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    for x in range(20,500):
        canvas.create_image(x, 10, image = gif1, tag = "pic")
        canvas.update()
        print('lololololo')
        # 暂停0.05妙，然后删除图像
        time.sleep(0.025)
        canvas.delete('pic')
        print('hahahahahaha')
