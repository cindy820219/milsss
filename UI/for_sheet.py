import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog
import for_parsing


def create_notes(measure, PI, staff_data, type_data):
    
    notes_measure_x = 263 + (measure-1)*230 + (PI*57.5)
    ### 3/4 PI and 4/4 PI
    #if ():

    #else ():
    #    notes_measure_x += 263 + (measure-1)*230 + (PI*57.5)

    ### about the y: left-hand and right-gand 
    if(staff_data == 1):
        notes_staff_y = 40
    
    else:
        notes_staff_y = 132

    if(type_data == 'quarter'):
        # print('is create_notes ',type_data )
        # quarter
        quarter = PhotoImage(file = 'quarter.gif')
        label_notes = Label(image = quarter)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = quarter # keep a reference!

    if(type_data == 'whole'):
        # print('is create_notes ',type_data )
        # whole
        whole = PhotoImage(file = 'whole.gif')
        label_notes = Label(image = whole)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = whole # keep a reference!

    if(type_data == 'eighth'):
        # print('is create_notes ',type_data )
        # eighth
        eight = PhotoImage(file = 'eighth.gif')
        label_notes = Label(image = eight)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = eight # keep a reference!
    
    if(type_data == '16th'):
        # print('is create_notes ',type_data )
        # six
        six = PhotoImage(file = '16th.gif')
        label_notes = Label(image = six)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = six # keep a reference!v

    if(type_data == 'half'):
        # print('is create_notes ',type_data )
        # half
        half = PhotoImage(file = 'half.gif')
        label_notes = Label(image = half)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = half # keep a reference!
        