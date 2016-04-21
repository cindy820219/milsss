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



anchor_pos_x_default    = 23
anchor_pos_y_default    = 20
anchor_pos_x_limit      = 885
# anchor_pos_x_stepping   = 0
anchor_pos_refresh_rate = 1
anchor_pos_x = anchor_pos_x_default
anchor_pos_y = anchor_pos_y_default



def anchor_move(canvas, gif1, anchor_pos_x, anchor_pos_y):
    #for x in range(23,885,2):
    canvas.delete('pic')
    canvas.create_image(anchor_pos_x, anchor_pos_y, image = gif1, tag = "pic")
    
    canvas.update()
    # 暂停0.05妙，然后删除图像
    #time.sleep(0.0025)
    #canvas.delete('pic')
    #canvas.update()

    anchor_pos_x += anchor_pos_x_stepping
    if (anchor_pos_x <= anchor_pos_x_limit):
        canvas.after(anchor_pos_refresh_rate, anchor_move, canvas, gif1, anchor_pos_x, anchor_pos_y)

def red_line(Tem):

    On = (60.0 / Tem ) * 0.5
    Off = On * 0.5

    global anchor_pos_x_stepping
    # if(beats == 3):
    #   anchor_pos_x_stepping  = Tem * 0.021
    # else:
    anchor_pos_x_stepping  = Tem * 0.021 * 0.75
    
    # print(anchor_pos_x_stepping)

    gif1 = PhotoImage(file = 'up.gif')
    gif2 = PhotoImage(file = 'up1.gif')
    gif3 = PhotoImage(file = 'up0.gif')

    # create the canvas, size in pixels
    canvas = Canvas(width = 920, height = 30) # bg = 'yellow')
    canvas.place(x= 270 ,y=0)


    canvas.create_image(23, 20, image = gif2, tag = "pic")
    canvas.update()
    time.sleep(0.2)

    ### count down
    for y in range(3):
        canvas.create_image(23, 20, image = gif2, tag = "pic")
        canvas.update()
        # delays for 5 seconds
        canvas.delete('pic')
        time.sleep(On)
        
        canvas.create_image(23, 20, image = gif3, tag = "pic")
        canvas.update()
        # 暂停0.05妙，然后删除图像
        # time.sleep(0.5)
        canvas.delete('pic')
        time.sleep(Off)
        
    canvas.create_image(anchor_pos_x, anchor_pos_y, image = gif1, tag = "pic")
    anchor_move(canvas, gif1, anchor_pos_x, anchor_pos_y)
    canvas.delete('pic')
    

    '''
    for x in range(23,885,2):
        canvas.create_image(x, 20, image = gif1, tag = "pic")
        canvas.update()
        # 暂停0.05妙，然后删除图像
        time.sleep(0.0025)
        canvas.delete('pic')
        #canvas.update()
  
    '''