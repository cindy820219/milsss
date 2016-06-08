import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

import for_sheet
import for_modify
import time

import for_metronome
import for_line

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

note_x = []
sort_note_x = []

def buttomPlay(filename ,Li, Pr, Pl, Tem, note_x):
    print('buttom note: ',note_x )
    print('len note: ',len(note_x))
    ### for beats
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection, note_x)

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
        # print('note_x.sort: ', sorted(note_x))
        
        sort_note_x = sorted(note_x)
        len_note_x = len(note_x)
        # print('sorted note_x: ', sort_note_x)
        # print(sort_note_x.pop(0))

        ### default canvas: create the canvas, size in pixels
        canvas = Canvas(width = 920, height = 30) # bg = 'yellow')
        canvas.place(x= 270 ,y=0)

        gif1 = PhotoImage(file = 'up.gif')
        gif2 = PhotoImage(file = 'up1.gif')
        gif3 = PhotoImage(file = 'up0.gif')

        for i in range (len_note_x):
            x = sort_note_x.pop(0) - 260 
            canvas.create_image(x, 20, image = gif2, tag = "pic")
            canvas.update()
            time.sleep(0.2)
            canvas.delete('pic')

    ### Play mode
    if (Pl ==1):
        print('Play mode')
        for_line.continue_line(Tem, filename, beats)