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

global notes_x
notes_x = []

def buttomPlay(filename ,Li, Pr, Pl, Tem, notes_x):

    ### for beats
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection)

    times = collection.getElementsByTagName('time')
    for beats in times:
        beats = beats.getElementsByTagName('beats')[0]
        beats = beats.childNodes[0].data


    # print('Li, Pr, Pl, Tem: ',Li, Pr, Pl, Tem)
    ### Listen mode
    if (Li == 1):
        print('Listen mode')
        for_line.continue_line(Tem, filename, beats)


    ### Practice mode 
    if (Pr == 1):
        print('Practice mode')
        print('notes_measure_x: ', notes_x)
        print('count: ', len(notes_x))


    ### Play mode
    if (Pl ==1):
        print('Play mode')
        for_line.continue_line(Tem, filename, beats)