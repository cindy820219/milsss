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


### Accidentals
def Accidentals(w, alter_data, notes_measure_x, notes_staff_y ,MIDI):
    # print('alter_data: ',alter_data)
    ### ###
    if(alter_data == 1):
        ### v
        w.create_line(notes_measure_x-6, notes_staff_y-4, notes_measure_x-6,  notes_staff_y+10, width=2)
        w.create_line(notes_measure_x-11, notes_staff_y-4, notes_measure_x-11,  notes_staff_y+10, width=2)
        ### h
        w.create_line(notes_measure_x-15, notes_staff_y+1, notes_measure_x-2,  notes_staff_y-1, width=2)
        w.create_line(notes_measure_x-15, notes_staff_y+8, notes_measure_x-2,  notes_staff_y+6, width=2)

        MIDI += 1
       

        # w.create_arc(coord, start=90, extent=100, fill="blue")
    
    ### bbb
    if(alter_data == -1):
        
        coord = notes_measure_x-17, notes_staff_y-7, notes_measure_x-4, notes_staff_y+8
        w.create_arc(coord, start=-90, extent=110, width=2) #, fill="blue")
        w.create_line(notes_measure_x-10, notes_staff_y-6, notes_measure_x-10,  notes_staff_y+8, width=2)

        MIDI -= 1

    if(alter_data == 0):
        ### v
        w.create_line(notes_measure_x-10, notes_staff_y-6, notes_measure_x-10,  notes_staff_y+8, width=2)
        w.create_line(notes_measure_x-5, notes_staff_y, notes_measure_x-5,  notes_staff_y+14, width=2)
        ### h
        w.create_line(notes_measure_x-11, notes_staff_y+1, notes_measure_x-4,  notes_staff_y-1, width=2)
        w.create_line(notes_measure_x-11, notes_staff_y+8, notes_measure_x-4,  notes_staff_y+6, width=2)

    return (MIDI)

def create_notes(w, measure, PI, staff_data, type_data, step_data, rhythm, octave_data, alter_data, beats_111, note_x, stem, MIDI_str, key_x_str, key_y_str, daul):

    # if (daul != ''):
    #     print('000000000000 dual : ',daul)

    ### Measure 1-4 : measure line
    measure_line_x0 = 20
    measure_line_y0 = 40
    measure_line_y1 = 77

    for i in range(1,5):
        w.create_line(measure_line_x0 + i*240, measure_line_y0, measure_line_x0 + i*240, measure_line_y1)
        w.create_line(measure_line_x0 + i*240, measure_line_y0+96, measure_line_x0 + i*240, measure_line_y1+96)

    if(measure >= 5):
        for i in range(1,5):
            w.create_line(measure_line_x0 + i*240, measure_line_y0+161, measure_line_x0 + i*240, measure_line_y1+161)
            w.create_line(measure_line_x0 + i*240, measure_line_y0+96+161, measure_line_x0 + i*240, measure_line_y1+96+161)


    ## w.create_line(20,  5,  20, 42)
    ## w.create_line(260, 5, 260, 42)
    ## w.create_line(500, 5, 500, 42)
    ## w.create_line(740, 5, 740, 42)
    ## w.create_line(980, 5, 980, 42)

    ## w.create_line(20,  101,  20, 138)
    ## w.create_line(260, 101, 260, 138)
    ## w.create_line(500, 101, 500, 138)
    ## w.create_line(740, 101, 740, 138)
    ## w.create_line(980, 101, 980, 138)


    ### measure 1-4 right
    ### line 5
    w.create_line(5, 5+35, 980, 5+35)
    ### line 4
    w.create_line(5, 14.5+35, 980, 14.5+35)
    ### line 3
    w.create_line(5, 24+35, 980, 24+35)
    ### line 2
    w.create_line(5, 33+35, 980, 33+35)
    ### line 1
    w.create_line(5, 42+35, 980, 42+35)

    ### measure 1-4 left
    ### line 5
    w.create_line(5, 101+35, 980, 101+35)
    ### line 4
    w.create_line(5, 110.5+35, 980, 110.5+35)
    ### line 3
    w.create_line(5, 120+35, 980, 120+35)
    ### line 2
    w.create_line(5, 129+35, 980, 129+35)
    ### line 1
    w.create_line(5, 138+35, 980, 138+35)
    

    ### measure 5-9 right
    ### right
    
    # x += 28
    if (5 <= measure and measure <= 9):
        ### line 5
        w.create_line(5, 166+35, 980, 166+35)
        ### line 4
        w.create_line(5, 175+35, 980, 175+35)
        ### line 3
        w.create_line(5, 184.5+35, 980, 184.5+35)
        ### line 2
        w.create_line(5, 193+35, 980, 193+35)
        ### line 1
        w.create_line(5, 202+35, 980, 202+35)
        ### measure 5-9 left
        ### line 5
        w.create_line(5, 261.5+35, 980, 261.5+35)
        ### line 4
        w.create_line(5, 271+35, 980, 271+35)
        ### line 3
        w.create_line(5, 280+35, 980, 280+35)
        ### line 2
        w.create_line(5, 289+35, 980, 289+35)
        ### line 1
        w.create_line(5, 298+35, 980, 298+35)

    ### draw the notes
    notes_staff_y = 0
    MIDI = 0


    ### 3/4 PI and 4/4 PI
    # notes_measure_x = 263 + (measure-1)*230 + (PI*57.5)
    # new notes_measure_x = 20 + (measure-1)*240 + (PI*60)
    if (beats_111 == 3):
        # notes_measure_x = 60 + (measure-1)*240 + ((PI-1)*60)
        notes_measure_x = 80 + (measure-1)*240 + ((PI-1)*60)
        
        ### measure 4-8
        if (4 < measure  and measure < 9):
            notes_measure_x = 80 + (measure-5)*240 + ((PI-1)*60)
        if (8 < measure  and measure < 13):
            notes_measure_x = 80 + (measure-9)*240 + ((PI-1)*60)
    ### 4/4 
    else: 
        # notes_measure_x = 60 + (measure-1)*240 + ((PI-1)*48)
        notes_measure_x = 60 + (measure-1)*240 + ((PI-1)*48)

        ### measure 4-8
        if (4 < measure  and measure < 9):
            notes_measure_x = 60 + (measure-5)*240 + ((PI-1)*48)  
        if (8 < measure  and measure < 13):
            notes_measure_x = 60 + (measure-9)*240 + ((PI-1)*48)

    ########@@@@@@@@@@@@@@@@@@@@@@@
    ### about the y: left-hand and right-hand 
    # right-hand 
    if(staff_data == 1):
        if(octave_data == 3):
            notes_staff_y = 78.5 +35
            # notes_staff_y = 87
            MIDI += 48

        if(octave_data == 4):
            # notes_staff_y = 60
            notes_staff_y = 47.5 +35
            MIDI += 60

        if(octave_data == 5):
            # notes_staff_y = 35
            notes_staff_y = 16 +35
            MIDI += 72

        if (4 < measure  and measure < 9):
            notes_staff_y = notes_staff_y + 160
        if (8 < measure  and measure < 13):
            notes_staff_y = notes_staff_y + 320

    # left-hand
    else:
        if(octave_data == 4):
            # notes_staff_y = 97
            notes_staff_y = 89 +35
            MIDI += 60

        if(octave_data == 3):
            notes_staff_y = 121 +35
            MIDI += 48
        
        if(octave_data == 2):
            notes_staff_y = 153 +35
            MIDI += 36

        if (4 < measure  and measure < 9):
            notes_staff_y = notes_staff_y + 160
        if (8 < measure  and measure < 13):
            notes_staff_y = notes_staff_y + 320

        ######################
        ### for stem == dowm and left-hand modify notes_staff_y 
        
        # if(stem == 'down'):
        #     notes_staff_y += 8

    '''
    if (4 < measure  and measure < 8):
        notes_staff_y = notes_staff_y + 160
    '''

    ### pitch : count the notes notes_staff_y
    # if (step_data == 'C'):
        # notes_staff_y = notes_staff_y
    if (step_data == 'D'):
        notes_staff_y -= 4.5
        MIDI += 2

    if (step_data == 'E'):
        notes_staff_y -= 9
        MIDI += 4

    if (step_data == 'F'):
        notes_staff_y -= 13.5
        MIDI += 5

    if (step_data == 'G'):
        notes_staff_y -= 18
        MIDI += 7

    if (step_data == 'A'):
        notes_staff_y -= 22.5
        MIDI += 9

    if (step_data == 'B'):
        notes_staff_y -= 27
        MIDI += 11
        

    ### rest notes !
    if (step_data == '[ ]'):
        if(staff_data == 1):
            notes_staff_y = 40
            if (4 < measure  and measure < 9):
                notes_staff_y = notes_staff_y + 160
            if (9 < measure  and measure < 13):
                notes_staff_y = notes_staff_y + 320

        else:
            notes_staff_y = 132
            if (4 < measure  and measure < 9):
                notes_staff_y = notes_staff_y + 160
            if (9 < measure  and measure < 13):
                notes_staff_y = notes_staff_y + 320

        if(type_data == 'quarter'):
            # quarter
            if (staff_data == 1):
                notes_staff_y -= 4
            ### line \
            w.create_line(notes_measure_x, notes_staff_y+4, notes_measure_x+6, notes_staff_y+12, width = 2)
            ### line /
            w.create_line(notes_measure_x+4, notes_staff_y+10, notes_measure_x, notes_staff_y+19, width = 3)
            ### line \
            w.create_line(notes_measure_x+1, notes_staff_y+16, notes_measure_x+4, notes_staff_y+24, width = 2)
            ### line -
            w.create_line(notes_measure_x-2, notes_staff_y+23, notes_measure_x+6, notes_staff_y+26, width = 2)

            ### arc c
            # coord = notes_measure_x-1, notes_staff_y+23, notes_measure_x+6, notes_staff_y+30
            coord = notes_measure_x-5, notes_staff_y+23, notes_measure_x+2, notes_staff_y+30
            w.create_arc(coord, start=110, extent=130, width=1, fill="black")
            ### line \
            w.create_line(notes_measure_x-2, notes_staff_y+30, notes_measure_x+6, notes_staff_y+34, width =2)

            # quarter = PhotoImage(file = 'rest_quarter.gif')
            # label_notes = Label(image = quarter)
            # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            # label_notes.place(x=notes_measure_x,y=notes_staff_y)
            # label_notes.image = quarter # keep a reference!

        if(type_data == '---'):
        # whole
            w.create_rectangle(notes_measure_x, notes_staff_y+15, notes_measure_x+15, notes_staff_y+20, fill='black')
            w.create_line(notes_measure_x-6, notes_staff_y+15, notes_measure_x+21, notes_staff_y+15, width = 2)

        if(type_data == 'eighth'):
            # eighth
            if(staff_data == 2):
                notes_staff_y += 4
            # ### .
            # w.create_oval(notes_measure_x+1, notes_staff_y+13, notes_measure_x+ 5, notes_staff_y+17, fill='black')
            # ### -
            # w.create_line(notes_measure_x+5, notes_staff_y+14, notes_measure_x+9, notes_staff_y+12)
            # ### /
            # w.create_line(notes_measure_x+9, notes_staff_y+9, notes_measure_x+7, notes_staff_y+24, width = 1)
            
            ### .
            w.create_oval(notes_measure_x-2, notes_staff_y+13, notes_measure_x+1, notes_staff_y+17, fill='black')
            ### -
            w.create_line(notes_measure_x+1, notes_staff_y+14, notes_measure_x+5, notes_staff_y+12)
            w.create_line(notes_measure_x+1, notes_staff_y+15, notes_measure_x+5, notes_staff_y+13)
            
            ### check if the chord
            
            ### /
            w.create_line(notes_measure_x+5, notes_staff_y+9, notes_measure_x+3, notes_staff_y+24, width = 1)
            w.create_line(notes_measure_x+5, notes_staff_y+10, notes_measure_x+3, notes_staff_y+25, width = 1)

        if(type_data == '16th'):
            # six
            # ### . . 
            # w.create_oval(notes_measure_x+1, notes_staff_y+13, notes_measure_x+ 4, notes_staff_y+16, fill='black')
            # w.create_oval(notes_measure_x-1, notes_staff_y+22, notes_measure_x+ 2, notes_staff_y+25, fill='black')
            # ### - 
            # ### -
            # w.create_line(notes_measure_x+4, notes_staff_y+13, notes_measure_x+8, notes_staff_y+11)
            # w.create_line(notes_measure_x+2, notes_staff_y+22, notes_measure_x+6, notes_staff_y+20)
            # ### /
            # w.create_line(notes_measure_x+7, notes_staff_y+11, notes_measure_x+4, notes_staff_y+30, width = 1)

            ### . . 
            w.create_oval(notes_measure_x-1, notes_staff_y+13, notes_measure_x+2, notes_staff_y+16, fill='black')
            w.create_oval(notes_measure_x-3, notes_staff_y+22, notes_measure_x, notes_staff_y+25, fill='black')
            ### - 
            ### -
            w.create_line(notes_measure_x+2, notes_staff_y+13, notes_measure_x+6, notes_staff_y+11)
            w.create_line(notes_measure_x, notes_staff_y+22, notes_measure_x+4, notes_staff_y+20)

            w.create_line(notes_measure_x+2, notes_staff_y+14, notes_measure_x+6, notes_staff_y+12)
            w.create_line(notes_measure_x, notes_staff_y+23, notes_measure_x+4, notes_staff_y+21)

            ### /
            w.create_line(notes_measure_x+5, notes_staff_y+11, notes_measure_x+2, notes_staff_y+30, width = 1)
            w.create_line(notes_measure_x+5, notes_staff_y+10, notes_measure_x+2, notes_staff_y+29, width = 1)

        if(type_data == 'half'):
            if (rhythm == 3.0):
                # half
                if(staff_data == 1):
                    notes_staff_y -= 4
                    
                w.create_rectangle(notes_measure_x, notes_staff_y+16, notes_measure_x+15, notes_staff_y+21, fill='black')
                w.create_line(notes_measure_x-6, notes_staff_y+23, notes_measure_x+21, notes_staff_y+23, width = 2)

                w.create_oval(notes_measure_x+22, notes_staff_y+17, notes_measure_x+25, notes_staff_y+20, fill = 'black')
            
            else:
                # half
                if(staff_data == 1):
                    notes_staff_y -= 4

                w.create_rectangle(notes_measure_x, notes_staff_y+16, notes_measure_x+15, notes_staff_y+21, fill='black')
                w.create_line(notes_measure_x-6, notes_staff_y+23, notes_measure_x+21, notes_staff_y+23, width = 2)
            
    ### notes !
    else:
        # quarter
        if(type_data == 'quarter'):
            
            if (stem == 'down'):
                w.create_line(notes_measure_x-1, notes_staff_y+1.5, notes_measure_x-1, notes_staff_y+26.5, width=2)

            else :
                w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+6.5, notes_staff_y+5.5, width=2)

            w.create_oval(notes_measure_x-2, notes_staff_y-1, notes_measure_x+6.5, notes_staff_y+7, fill='black')
            
            ### midle sol
            # w.create_oval(80, 29.5, 88.5, 36.5, fill='black')
            ### midle sol two PI
            # w.create_oval(140, 29.5, 149, 36.5, fill='black')
            ### midle sol three PI
            # w.create_oval(200, 29.5, 209, 36.5, fill='black')

            # w.create_oval(160,89, 169, 96, fill='black')
            # w.create_line(155,93,174.5,93,  width=2)

            # w.create_oval(140, 93.5, 148.5, 100.5, fill='black')

            ### midle Mi
            # w.create_oval(140, 6.5, 148.5, 13.5, fill='black')
            # w.create_oval(140,102.5, 148.5, 109.5, fill='black')

            ### midle Do
            # w.create_oval(120, 16, 128.5, 23, fill='black')
            # w.create_oval(120, 16+96, 128.5, 23+96, fill='black')
            # w.create_oval(120, 112, 128.5, 119, fill='black')

            ### midle La
            # w.create_oval(100,25,109,32, fill='black')
            # w.create_oval(100,25+96,109,32+96, fill='black')
            # w.create_oval(100,121,109,128, fill='black')

            ### midle Fa
            # w.create_oval(60,34,68.5,41, fill='black')
            # w.create_oval(60,34+96,68.5,41+96, fill='black')
            # w.create_oval(60,34+160,68.5, 41+160, fill='black')
            # w.create_line(0, 0, 400, 400)

            ### midle Re
            # w.create_oval(40,43,48.5,50, fill='black')

            ### midle Do
            # w.create_oval(20,47.5,29, 56, fill='black')
            # w.create_line(15, 53, 35, 53,  width=2)

        # whole
        if(type_data == 'whole'):
            w.create_oval(notes_measure_x-2, notes_staff_y-1, notes_measure_x+6.5, notes_staff_y+7, width=1.5)
        
        ### eighth
        if(type_data == 'eighth'):
            if (stem == 'down'):
                ### |
                w.create_line(notes_measure_x-1, notes_staff_y+1.5, notes_measure_x-1, notes_staff_y+26.5, width=2)
                if (daul == ''):
                    ### /
                    w.create_line(notes_measure_x-1, notes_staff_y+26.5, notes_measure_x+7, notes_staff_y+17, width = 2)
                    ### \
                    w.create_line(notes_measure_x+7, notes_staff_y+17, notes_measure_x+5, notes_staff_y+10, width = 2)
                    
                # else: 
                #     w.create_line(notes_measure_x-1, notes_staff_y+26.5, notes_measure_x+7, notes_staff_y+17, width = 2)

            ### stem == UP
            else:
                if (daul == ''):
                #     print('INNNNNNNNNNNNNN')
                    # pre_eight_x0 = notes_measure_x+6.5
                    # pre_eight_y0 = notes_staff_y-20.5
                    # pre_eight_x1 = notes_measure_x+14.5
                    # pre_eight_y1 = notes_staff_y-11

                    pre_eight_x0 = 0
                    pre_eight_y0 = 0
                    pre_eight_x1 = 1000
                    pre_eight_y1 = 1000


                if (daul != ''):
                    # print('hahahahahah', pre_eight_x0, pre_eight_y0, pre_eight_x1, pre_eight_y1)
                    # w.create_line(pre_eight_x0, pre_eight_y0, pre_eight_x1, pre_eight_y1, width = 4, fill='white')
                    w.create_line(0, 0, 1000,100, width = 4)
                    print('IM innnnnnnnnnn')
                    print('INNNNNNNNNNNNNN')

                ### |
                w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+6.5, notes_staff_y+5.5, width=2)
                # if (daul != ''):
                #     # print('000000000000 dual : ',daul)
                ### \
                w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+14.5, notes_staff_y-11, width = 2)
                ### /
                w.create_line(notes_measure_x+14.5, notes_staff_y-11, notes_measure_x+12.5, notes_staff_y-4, width = 2)

            

               
                
                # print('hahahahahah', pre_eight_x0, pre_eight_y0, pre_eight_x1, pre_eight_y1)

            w.create_oval(notes_measure_x-2, notes_staff_y-1, notes_measure_x+6.5, notes_staff_y+7, fill='black')
            
           
        if(type_data == '16th'):
            # six
            if (stem == 'down'):
                w.create_line(notes_measure_x-1, notes_staff_y+1.5, notes_measure_x-1, notes_staff_y+26.5, width=2)
                
                if (daul == ''):
                    ### / more strong
                    w.create_line(notes_measure_x-1, notes_staff_y+26.5, notes_measure_x+6, notes_staff_y+16.5, width = 1)
                    w.create_line(notes_measure_x-1, notes_staff_y+24.5, notes_measure_x+6, notes_staff_y+15.5, width = 1)
                    ### |
                    # w.create_line(notes_measure_x+5, notes_staff_y+17, notes_measure_x+3, notes_staff_y+10, width = 1)

                    ### / more strong
                    w.create_line(notes_measure_x-1, notes_staff_y+20.5, notes_measure_x+6, notes_staff_y+10.5, width = 1)
                    w.create_line(notes_measure_x-1, notes_staff_y+18.5, notes_measure_x+6, notes_staff_y+9.5, width = 1)
                    ### |
                    # w.create_line(notes_measure_x+5, notes_staff_y+13, notes_measure_x+3, notes_staff_y+4, width = 1)
                # if (daul != ''):

            ### UP 
            else:
                w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+6.5, notes_staff_y+5.5, width=2)
                ### \ 
                w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+11.5, notes_staff_y-10, width = 1)
                w.create_line(notes_measure_x+6.5, notes_staff_y-18.5, notes_measure_x+11.5, notes_staff_y-9, width = 1)
                ### |
                # w.create_line(notes_measure_x+12.5, notes_staff_y-11, notes_measure_x+10.5, notes_staff_y-4, width = 1)
                ### \ 
                w.create_line(notes_measure_x+6.5, notes_staff_y-14.5, notes_measure_x+11.5, notes_staff_y-4, width = 1)
                w.create_line(notes_measure_x+6.5, notes_staff_y-12.5, notes_measure_x+11.5, notes_staff_y-3, width = 1)
                ### |
                # w.create_line(notes_measure_x+12.5, notes_staff_y-9, notes_measure_x+10.5, notes_staff_y-2, width = 1)
        
            w.create_oval(notes_measure_x-2, notes_staff_y-1, notes_measure_x+6.5, notes_staff_y+7, fill='black')

        if(type_data == 'half'):
            ### third 
            if (rhythm == 3.0):
                if (stem == 'down'):
                    w.create_line(notes_measure_x-1, notes_staff_y+1.5, notes_measure_x-1, notes_staff_y+26.5, width=2)
                    w.create_oval(notes_measure_x+11, notes_staff_y+2, notes_measure_x+13, notes_staff_y+5, fill = 'black')

                else:
                    w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+6.5, notes_staff_y+5.5, width=2)
                    w.create_oval(notes_measure_x+11, notes_staff_y+2, notes_measure_x+14, notes_staff_y+5, fill = 'black')

                w.create_oval(notes_measure_x-2, notes_staff_y-1, notes_measure_x+7, notes_staff_y+7, width=2)

            else:
                # half
                if (stem == 'down'):
                    w.create_line(notes_measure_x-1, notes_staff_y+1.5, notes_measure_x-1, notes_staff_y+26.5, width=2)
                else: 
                    w.create_line(notes_measure_x+6.5, notes_staff_y-20.5, notes_measure_x+6.5, notes_staff_y+5.5, width=2)

                w.create_oval(notes_measure_x-2, notes_staff_y-1, notes_measure_x+7, notes_staff_y+7, width=2)
            
        
        MIDI_fianl = Accidentals(w, alter_data, notes_measure_x, notes_staff_y, MIDI)
        key_location(MIDI_fianl, key_x_str, key_y_str)
        # MIDI_fianl = str(MIDI_fianl)
        # print('MIDI_fianl: ',MIDI_fianl)
        MIDI_str.append(MIDI_fianl)

    note_x.append(notes_measure_x)
    # print('MIDI_str: ', MIDI_str)
    # print('note_x :', note_x)
