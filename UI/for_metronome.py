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

def metronome():
    
    metronome = PhotoImage(file = 'quarter.gif')
    label_metronome = Label(image = metronome)
    # print(move)  
    label_metronome.place (x=60, y=250)
    label_metronome.image = metronome # keep a reference!

    time.sleep(30)
    metronome = PhotoImage(file = 'quarter.gif')
    label_metronome = Label(image = metronome)
    label_metronome.place (x=360, y=250)
    label_metronome.image = metronome # keep a reference!
