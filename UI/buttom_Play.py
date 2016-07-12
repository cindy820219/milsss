import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import tkinter.filedialog as filedialog

from xml.dom.minidom import parse
import xml.dom.minidom

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

import time

import for_parsing
import for_sheet
import for_modify

note_x = []
sort_note_x = []

note_x_1 = []

MIDI_str = []
key_str = []

def buttomPlay(filename ,Li, Pr, Pl, Tem, note_x, key_x_str, key_y_str, hands):
    # print('buttom note: ',note_x )
    # print('len note: ',len(note_x))
    note_x = []
    ### for beats
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection, note_x, MIDI_str, key_x_str, key_y_str, hands)
    # collection, note_x, MIDI_str, key_x_str, key_y_str

    times = collection.getElementsByTagName('time')
    for beats in times:
        beats = beats.getElementsByTagName('beats')[0]
        beats = beats.childNodes[0].data

    # print('note_x = []', note_x )

    # print('Li, Pr, Pl, Tem: ',Li, Pr, Pl, Tem)
    ### Listen mode
    if (Li == 1):
        print('Listen mode')
        for_line.continue_line(Tem, filename, beats)

    
    ### Practice mode 
    if (Pr == 1):
        print('Practice mode')
        # print('note_x: ',note_x)
        # print(len(note_x))
        lenth = len(note_x)
        # print('note_x.sort: ', sorted(note_x))
        
        ### for 5-9 str of notes!!! 
        for i in range(len(note_x)-1):
            if((note_x[i]) - (note_x[i+1]) > 460 ):
                # print('!!!!!! there must next string: ',note_x[i], note_x[i+1])
                # note_x_1.append(note_x[i+1])
                # print('note_x_1: ',note_x_1)
                # print(note_x[i+1], note_x[lenth-1])
                ### print(note_x[(i+1):(lenth-1)])
                
                note_x_1 = note_x[ (i+1) : (lenth-1) ]
                note_x = note_x[0: i]

                # print('note_x: ',note_x)
                # print('note_x_1: ',note_x_1)

                break

        ### note_x -----------------------------------------------
        gif2 = PhotoImage(file = 'up1.gif')
        sort_note_x = sorted(note_x)
        len_note_x = len(note_x)
        # print('sorted note_x: ', sort_note_x)
        # print(sort_note_x.pop(0))

        ### default canvas: create the canvas, size in pixels
        canvas = Canvas(width = 920, height = 30) # bg = 'yellow')
        canvas.place(x= 270 ,y=-10)

        for i in range (len_note_x):
            x = sort_note_x.pop(0) - 260 
            canvas.create_image(x, 20, image = gif2, tag = "pic")
            canvas.update()
            time.sleep(0.2)
            canvas.delete('pic')
        ### -------------------------------------------------------

        ### note_x_1 ----------------------------------------------
        sort_note_x_1 = sorted(note_x_1)
        len_note_x_1 = len(note_x_1)
        # print('sorted note_x: ', sort_note_x)
        # print(sort_note_x.pop(0))

        ### default canvas: create the canvas, size in pixels
        canvas = Canvas(width = 920, height = 30) # bg = 'yellow')
        canvas.place(x= 270 ,y= 160)

        for i in range (len_note_x_1):
            x = sort_note_x_1.pop(0) - 260 
            canvas.create_image(x, 20, image = gif2, tag = "pic")
            canvas.update()
            time.sleep(0.2)
            canvas.delete('pic')

        ### -------------------------------------------------------


    ### Play mode
    if (Pl ==1):
        print('Play mode')
        # for_line.continue_line(Tem, filename, beats)