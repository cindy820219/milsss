import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog
import for_parsing

'''
def create_sheet(beats ='4'):
    if (beats == '4'):
        photo = PhotoImage(file = '4.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=20)
        label_sheet.image = photo # keep a reference!

        photo = PhotoImage(file = '4.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=180)
        label_sheet.image = photo # keep a reference!

        photo = PhotoImage(file = '4.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=340)
        label_sheet.image = photo # keep a reference!
        create_notes()

    if(beats == '3'):
        photo = PhotoImage(file = '3.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=20)
        label_sheet.image = photo # keep a reference!

        photo = PhotoImage(file = '3.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=180)
        label_sheet.image = photo # keep a reference!

        photo = PhotoImage(file = '3.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=340)
        label_sheet.image = photo # keep a reference!

        create_notes()

    if(beats == '6'):
        photo = PhotoImage(file = '6.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=20)
        label_sheet.image = photo # keep a reference!

        photo = PhotoImage(file = '6.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=180)
        label_sheet.image = photo # keep a reference!

        photo = PhotoImage(file = '6.gif')
        label_sheet = Label(image = photo)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_sheet.place(x=200,y=340)
        label_sheet.image = photo # keep a reference!

        create_notes()
'''

def create_notes(type_data):

    if(type_data == 'quarter'):
        print('is create_notes ',type_data )
        # quarter
        quarter = PhotoImage(file = 'quarter.gif')
        label_notes = Label(image = quarter)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=723,y=40)
        label_notes.image = quarter # keep a reference!

    if(type_data == 'whole'):
        print('is create_notes ',type_data )
        # whole
        whole = PhotoImage(file = 'whole.gif')
        label_notes = Label(image = whole)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=608,y=40)
        label_notes.image = whole # keep a reference!

    if(type_data == 'eighth'):
        print('is create_notes ',type_data )
        # eighth
        eight = PhotoImage(file = 'eighth.gif')
        label_notes = Label(image = eight)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=665.5,y=40)
        label_notes.image = eight # keep a reference!
    
    if(type_data == '16th'):
        print('is create_notes ',type_data )
        # six
        six = PhotoImage(file = '16th.gif')
        label_notes = Label(image = six)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=953,y=40)
        label_notes.image = six # keep a reference!v

    if(type_data == 'half'):
        print('is create_notes ',type_data )
        # half
        half = PhotoImage(file = 'half.gif')
        label_notes = Label(image = half)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=783,y=40)
        label_notes.image = half # keep a reference!
        