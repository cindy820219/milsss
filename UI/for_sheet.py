import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog
import for_parsing


def create_notes(measure, PI, staff_data, type_data, step_data, rhythm, octave_data):
    
    notes_measure_x = 263 + (measure-1)*230 + (PI*57.5)
    ### 3/4 PI and 4/4 PI
    #if ():

    #else ():
    #    notes_measure_x += 263 + (measure-1)*230 + (PI*57.5)

    ### about the y: left-hand and right-hand 
    # right-hand 
    if(staff_data == 1):
        if(octave_data == 4):
            notes_staff_y = 60

        if(octave_data == 5):
            notes_staff_y = 35

    # left-hand
    else:
        if(octave_data == 3):
            notes_staff_y = 132
        
        if(octave_data == 2):
            notes_staff_y = 167
        
    ### pitch : count the notes notes_staff_y
    # if (step_data == 'C'):
        # notes_staff_y = notes_staff_y
    if (step_data == 'D'):
        notes_staff_y -= 5
    if (step_data == 'E'):
        notes_staff_y -= 10
    if (step_data == 'F'):
        notes_staff_y -= 15
    if (step_data == 'G'):
        notes_staff_y -= 20
    if (step_data == 'A'):
        notes_staff_y -= 25
    if (step_data == 'B'):
        notes_staff_y -= 30
        

    ### rest notes !
    if (step_data == '[ ]'):
        if(staff_data == 1):
            notes_staff_y = 40
        else:
            notes_staff_y = 132

        if(type_data == 'quarter'):
        # quarter
            quarter = PhotoImage(file = 'rest_quarter.gif')
            label_notes = Label(image = quarter)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = quarter # keep a reference!

        if(type_data == 'whole'):
            # whole
            whole = PhotoImage(file = 'rest_whole.gif')
            label_notes = Label(image = whole)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = whole # keep a reference!

        if(type_data == 'eighth'):
            # eighth
            eight = PhotoImage(file = 'rest_eighth.gif')
            label_notes = Label(image = eight)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = eight # keep a reference!
        
        if(type_data == '16th'):
            # six
            six = PhotoImage(file = 'rest_16th.gif')
            label_notes = Label(image = six)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = six # keep a reference!v

        if(type_data == 'half'):
            if (rhythm == 3.0):
                half = PhotoImage(file = 'rest_third.gif')
                label_notes = Label(image = half)
                label_notes.place(x=notes_measure_x,y=notes_staff_y)
                label_notes.image = half
            
            else:
                # half
                half = PhotoImage(file = 'rest_half.gif')
                label_notes = Label(image = half)
                label_notes.place(x=notes_measure_x,y=notes_staff_y)
                label_notes.image = half # keep a reference!
            
    ### notes !
    else:
        if(type_data == 'quarter'):
            # quarter
            quarter = PhotoImage(file = 'quarter.gif')
            label_notes = Label(image = quarter)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = quarter # keep a reference!

        if(type_data == 'whole'):
            # whole
            whole = PhotoImage(file = 'whole.gif')
            label_notes = Label(image = whole)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = whole # keep a reference!

        if(type_data == 'eighth'):
            # eighth
            eight = PhotoImage(file = 'eighth.gif')
            label_notes = Label(image = eight)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = eight # keep a reference!
        
        if(type_data == '16th'):
            # six
            six = PhotoImage(file = '16th.gif')
            label_notes = Label(image = six)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = six # keep a reference!v

        if(type_data == 'half'):
            print(rhythm)
            ### third 
            if (rhythm == 3.0):
                half = PhotoImage(file = 'third.gif')
                label_notes = Label(image = half)
                label_notes.place(x=notes_measure_x,y=notes_staff_y)
                label_notes.image = half
            
            else:
                # half
                half = PhotoImage(file = 'half.gif')
                label_notes = Label(image = half)
                label_notes.place(x=notes_measure_x,y=notes_staff_y)
                label_notes.image = half # keep a reference!
            