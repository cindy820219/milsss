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

    # create the canvas, size in pixels
    canvas = Canvas(width = 920, height = 30) # bg = 'yellow')
    canvas.place(x= 270 ,y=0)

    gif1 = PhotoImage(file = 'up.gif')
    gif2 = PhotoImage(file = 'up1.gif')
    gif3 = PhotoImage(file = 'up2111.gif')

    canvas.create_image(23, 20, image = gif2, tag = "pic")
    canvas.update()
    time.sleep(0.2)

    for y in range(3):
        canvas.create_image(23, 20, image = gif2, tag = "pic")
        canvas.update()
        # delays for 5 seconds
        canvas.delete('pic')
        time.sleep(0.6)
        
        canvas.create_image(23, 20, image = gif3, tag = "pic")
        canvas.update()
        # 暂停0.05妙，然后删除图像
        # time.sleep(0.5)
        canvas.delete('pic')
        time.sleep(0.4)
        

    for x in range(23,885):
        x = x +1.1805555550000002
        canvas.create_image(x, 20, image = gif1, tag = "pic")
        canvas.update()
        # 暂停0.05妙，然后删除图像
        time.sleep(0.0025)
        canvas.delete('pic')


    '''
    photo = PhotoImage(file = 'red_line.gif')
    label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_sheet.place(x=20,y=30)
    label_sheet.image = photo # keep a reference!


    label_sheet.place(x=50,y=30)
    label_sheet.image = photo # keep a reference!

    
    for x in range(20,500):
        print('a')
        label_sheet.place(x=x,y=30)
        time.sleep(0.025)
        print('b')
        label_sheet.image = photo # keep a reference!
        print('c')
        time.sleep(0.025)
        print('----')
    '''
