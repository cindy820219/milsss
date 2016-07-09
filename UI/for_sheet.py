
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog
import for_parsing

global MIDI_str
global key_x_str, key_y_str

MIDI_str = []
key_x_str = []
key_y_str = []

def key_location(MIDI_fianl, key_x_str, key_y_str):
    # MIDI_fianl 

    key_note_x = 0
    key_note_y = 0

    note_name = MIDI_fianl % 12
    octave = MIDI_fianl // 12 - 3

    ### C
    if(note_name == 0):
        key_note_x = 402 + 134 * octave
        key_note_y = 650

    ### D
    if(note_name == 2):
        key_note_x = 422 + 134 * octave
        key_note_y = 650

    ### E
    if(note_name == 4):
        key_note_x = 441 + 134 * octave
        key_note_y = 650

    ### F
    if(note_name == 5):
        key_note_x = 459 + 134 * octave
        key_note_y = 650

    ### G
    if(note_name == 7):
        key_note_x = 478 + 134 * octave
        key_note_y = 650

    ### A
    if(note_name == 9):
        key_note_x = 497 + 134 * octave
        key_note_y = 650

    ### B
    if(note_name == 11):
        key_note_x = 517 + 134 * octave
        key_note_y = 650
    
    
    ###### ###
    ### C#
    if(note_name == 1):
        key_note_x = 412 + 134 * octave
        key_note_y = 705

    ### D#
    if(note_name == 2):
        key_note_x = 433 + 134 * octave
        key_note_y = 705

    ### F#
    if(note_name == 3):
        key_note_x = 412 + 134 * octave
        key_note_y = 705

    ### G#
    if(note_name == 4):
        key_note_x = 468 + 134 * octave
        key_note_y = 705

    ### A#
    if(note_name == 5):
        key_note_x = 487 + 134 * octave
        key_note_y = 705

    ### B#
    if(note_name == 6):
        key_note_x = 505 + 134 * octave
        key_note_y = 705

    # key_note_x = str(key_note_x)
    # key_note_y = str(key_note_y)
    key_x_str.append(key_note_x)
    key_y_str.append(key_note_y)

    # print('key_x_str, key_y_str: ', key_x_str, key_y_str)
    
    ### -------------------------------------- ###
    ### test!
    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=402, y=705)
    # label_notes.image = left # keep a reference!


    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=422, y=705)
    # label_notes.image = left # keep a reference!


    # right = PhotoImage(file = 'right.gif')
    # label_notes = Label(image = right)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=441, y=705)
    # label_notes.image = right # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=459, y=705)
    # label_notes.image = left # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=478, y=705)
    # label_notes.image = left # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=497, y=705)
    # label_notes.image = left # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=517, y=705)
    # label_notes.image = left # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=536, y=705)
    # label_notes.image = left # keep a reference!

    # #####################################


    # right = PhotoImage(file = 'right.gif')
    # label_notes = Label(image = right)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=412, y=650)
    # label_notes.image = right # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=433, y=650)
    # label_notes.image = left # keep a reference!

    # right = PhotoImage(file = 'right.gif')
    # label_notes = Label(image = right)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=468, y=650)
    # label_notes.image = right # keep a reference!

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=487, y=650)
    # label_notes.image = left # keep a reference!

    # right = PhotoImage(file = 'right.gif')
    # label_notes = Label(image = right)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=505, y=650)
    # label_notes.image = right # keep a reference!

    # right = PhotoImage(file = 'right.gif')
    # label_notes = Label(image = right)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=412+134, y=650)
    # label_notes.image = right # keep a reference!

    # key_x.append()

    ### -------------------------------------- ###

### Accidentals
def Accidentals(alter_data, notes_measure_x, notes_staff_y ,MIDI):

    ### ###
    if(alter_data == 1):
        notes_measure_x = notes_measure_x - 12
        notes_staff_y = notes_staff_y + 1
        up = PhotoImage(file = 'accidentals_#.gif')
        label_notes = Label(image = up)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = up # keep a reference!

        MIDI += 1

    
    ### bbb
    if(alter_data == -1):
        notes_measure_x = notes_measure_x -12
        down = PhotoImage(file = 'accidentals_b.gif')
        label_notes = Label(image = down)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = down # keep a reference!

        MIDI -= 1

    if(alter_data == 0):
        notes_measure_x = notes_measure_x - 12
        notes_staff_y = notes_staff_y + 2
        re = PhotoImage(file = 'accidentals_r.gif')
        label_notes = Label(image = re)
        #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        label_notes.place(x=notes_measure_x,y=notes_staff_y)
        label_notes.image = re # keep a reference!

    return (MIDI)

def create_notes(measure, PI, staff_data, type_data, step_data, rhythm, octave_data, alter_data, beats_111, note_x, stem, MIDI_str, key_x_str, key_y_str):

    notes_staff_y = 0
    MIDI = 0

    # notes_measure_x = 263 + (measure-1)*230 + (PI*57.5)
    if (beats_111 == 3):
        notes_measure_x = 293 + (measure-1)*230 + ((PI-1)*70)
        
        ### measure 4-8
        if (4 < measure  and measure < 9):
            notes_measure_x = 293 + (measure-5)*230 + ((PI-1)*70)
        if (8 < measure  and measure < 13):
            notes_measure_x = 293 + (measure-9)*230 + ((PI-1)*70)

    ### 3/4 PI and 4/4 PI
    else: 
        notes_measure_x = 293 + (measure-1)*230 + ((PI-1)*53.125)
        ### measure 4-8
        if (4 < measure  and measure < 9):
            notes_measure_x = 293 + (measure-5)*230 + ((PI-1)*53.125)  
        if (8 < measure  and measure < 13):
            notes_measure_x = 293 + (measure-9)*230 + ((PI-1)*70)


    ### about the y: left-hand and right-hand 
    # right-hand 
    if(staff_data == 1):
        if(octave_data == 3):
            notes_staff_y = 85
            MIDI += 48

        if(octave_data == 4):
            notes_staff_y = 60
            MIDI += 60

        if(octave_data == 5):
            notes_staff_y = 35
            MIDI += 72

        if (4 < measure  and measure < 9):
            notes_staff_y = notes_staff_y + 160
        if (8 < measure  and measure < 13):
            notes_staff_y = notes_staff_y + 320

    # left-hand
    else:
        if(octave_data == 4):
            notes_staff_y = 97
            MIDI += 60

        if(octave_data == 3):
            notes_staff_y = 132
            MIDI += 48
        
        if(octave_data == 2):
            notes_staff_y = 167
            MIDI += 36

        if (4 < measure  and measure < 9):
            notes_staff_y = notes_staff_y + 160
        if (8 < measure  and measure < 13):
            notes_staff_y = notes_staff_y + 320

        ######################
        ### for stem == dowm and left-hand modify notes_staff_y 
        if(stem == 'down'):
            notes_staff_y += 8

    '''
    if (4 < measure  and measure < 8):
        notes_staff_y = notes_staff_y + 160
    '''

    ### pitch : count the notes notes_staff_y
    # if (step_data == 'C'):
        # notes_staff_y = notes_staff_y
    if (step_data == 'D'):
        notes_staff_y -= 5
        MIDI += 2

    if (step_data == 'E'):
        notes_staff_y -= 10
        MIDI += 4

    if (step_data == 'F'):
        notes_staff_y -= 15
        MIDI += 5

    if (step_data == 'G'):
        notes_staff_y -= 20
        MIDI += 7

    if (step_data == 'A'):
        notes_staff_y -= 25
        MIDI += 9

    if (step_data == 'B'):
        notes_staff_y -= 30
        MIDI += 11
        

    ### rest notes !
    if (step_data == '[ ]'):
        if(staff_data == 1):
            notes_staff_y = 40
            if (4 < measure  and measure < 8):
                notes_staff_y = notes_staff_y + 160
            if (9 < measure  and measure < 12):
                notes_staff_y = notes_staff_y + 320

        else:
            notes_staff_y = 132
            if (4 < measure  and measure < 8):
                notes_staff_y = notes_staff_y + 160
            if (9 < measure  and measure < 12):
                notes_staff_y = notes_staff_y + 320

        if(type_data == 'quarter'):
        # quarter
            quarter = PhotoImage(file = 'rest_quarter.gif')
            label_notes = Label(image = quarter)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = quarter # keep a reference!

        if(type_data == '---'):
        # whole
            whole = PhotoImage(file = 'rest_whole.gif')
            label_notes = Label(image = whole)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = whole # keep a reference!

        # if(type_data == 'whole'):
        #     # whole
        #     whole = PhotoImage(file = 'rest_whole.gif')
        #     label_notes = Label(image = whole)
        #     #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        #     label_notes.place(x=notes_measure_x,y=notes_staff_y)
        #     label_notes.image = whole # keep a reference!


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
        # quarter
        if(type_data == 'quarter'):
            if (stem == 'down'):
                quarter = PhotoImage(file = 'quarter_d.gif')
            else :
                quarter = PhotoImage(file = 'quarter.gif')

            label_notes = Label(image = quarter)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = quarter # keep a reference!

            # Accidentals(alter_data, notes_measure_x, notes_staff_y)

        # whole
        if(type_data == 'whole'):
            whole = PhotoImage(file = 'whole.gif')
            label_notes = Label(image = whole)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = whole # keep a reference!

            # Accidentals(alter_data, notes_measure_x, notes_staff_y)

        # eighth
        if(type_data == 'eighth'):
            if (stem == 'down'):
                eight = PhotoImage(file = 'eighth_d.gif')
            else:
                eight = PhotoImage(file = 'eighth.gif')

            label_notes = Label(image = eight)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = eight # keep a reference!

            # Accidentals(alter_data, notes_measure_x, notes_staff_y)
        
        if(type_data == '16th'):
            # six
            if (stem == 'down'):
                six = PhotoImage(file = '16th_d.gif')
            else:
                six = PhotoImage(file = '16th.gif')
            
            label_notes = Label(image = six)
            label_notes.place(x=notes_measure_x,y=notes_staff_y)
            label_notes.image = six # keep a reference!v

            # Accidentals(alter_data, notes_measure_x, notes_staff_y)

        if(type_data == 'half'):
            ### third 
            if (rhythm == 3.0):
                if (stem == 'down'):
                    half = PhotoImage(file = 'third_d.gif')
                else:
                    half = PhotoImage(file = 'third.gif')

                label_notes = Label(image = half)
                label_notes.place(x=notes_measure_x,y=notes_staff_y)
                label_notes.image = half

                # Accidentals(alter_data, notes_measure_x, notes_staff_y)
            
            else:
                # half
                if (stem == 'down'):
                    half = PhotoImage(file = 'half_d.gif')
                else: 
                    half = PhotoImage(file = 'half.gif')

                label_notes = Label(image = half)
                label_notes.place(x=notes_measure_x,y=notes_staff_y)
                label_notes.image = half

                # Accidentals(alter_data, notes_measure_x, notes_staff_y)
        
        MIDI_fianl = Accidentals(alter_data, notes_measure_x, notes_staff_y, MIDI)
        key_location(MIDI_fianl, key_x_str, key_y_str)
        # MIDI_fianl = str(MIDI_fianl)
        # print('MIDI_fianl: ',MIDI_fianl)
        MIDI_str.append(MIDI_fianl)

    note_x.append(notes_measure_x)
    # print('MIDI_str: ', MIDI_str)
    # print('note_x :', note_x)
