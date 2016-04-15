from xml.dom.minidom import parse
import xml.dom.minidom
import math
import for_sheet

import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

import for_sheet


beats = 0
max_measure =0

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
        
        # create_notes()

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

        # create_notes()

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

        # create_notes()

### funtion pasing xml file
def parsing(collection):
    max_measure =0

    pre_staff = 0
    measure = 1

    pre_x_1 = pre_x_2 = ''
    pre_step_data = pre_octave_data = ''

    # about the mini_rhythm for the simple
    mini_rhythm = 6

    # about the ID
    # ID = ''

    # about the (time.rhythm / measure)
    timing = 0
    flag_of_daul = 0

    single_measure = 1
    single_time = 0
    single_pre_x = ''

    single_flag_of_daul = 0

    hand = 1

    note_num = 0

    ### to defind the sheet: key && divs && time
    attrs = collection.getElementsByTagName('attributes')
    
    for attr in attrs:
        divs = collection.getElementsByTagName('divisions')
        for div in divs:
            divisions = div.childNodes[0].data
            # print('divisions:' ,divisions)

        keys = collection.getElementsByTagName('key')
        for key in keys:
            fifths = key.getElementsByTagName('fifths')[0]

            fifths = fifths.childNodes[0].data
            print('key:' ,fifths)

        times = collection.getElementsByTagName('time')
        for time in times:
            beats = time.getElementsByTagName('beats')[0]
            beattype = time.getElementsByTagName('beat-type')[0]

            beats = beats.childNodes[0].data
            beattype = beattype.childNodes[0].data

            print('times: ',beats+'/'+beattype+' ')
            
            ### create_sheet
            create_sheet(beats)

        #print(beats)
        if ((int(beats) == 6) and (int(beattype) ==8)):
            beats = 3
            return(beats)

    ### about the tempo
    directions = collection.getElementsByTagName('direction')
    # direction(directions)
    for direction in directions:
        per_minute = collection.getElementsByTagName('per-minute')[0]
        per_minute = per_minute.childNodes[0].data
        # print('view_tempo: ',per_minute)


    sounds = collection.getElementsByTagName('sound')
    # sound(sounds)
    # print(sounds)
    for sound in sounds:
        if (sound.hasAttribute('tempo')):
            sound = sound.getAttribute('tempo')
            print('tempo: ',sound)
    
    ##################################################
    ### if no set tempo ! add new node about tempo !!!
    #if (sounds == []):
     #   add_tempo_node()
#
    
    
    ### print about the pitch type staff rhyth
    print('pitch\t\ttype\t\tstaff\t\trhythm')

    ### notes is a list
    notes = collection.getElementsByTagName('note')
    print('1=======================================================================')

    for note in notes:
        # if note.hasAttribute('default-x'):
        #   print('default-x: %s' % note.getAttribute('default-x'))
        note_num = int(note_num) + 1

        daul = ''
        close_daul = 0

        pitch = step_data = octave_data = type_data = staff_next_data  = staff_data = alter_data = ''

        duration = note.getElementsByTagName('duration')[0]
        rhythm = str(float(duration.childNodes[0].data)/float(divisions))
        
        if(timing >= int(beats) and (hand != 1)):
            # print('=======================================================================')
            # single_measure += 1
            timing = 0

        if (note.getElementsByTagName('accidental')):
            accidental = note.getElementsByTagName('accidental')[0]
            # alter_data = accidental.childNodes[0].data
            alter_data = '0'

        ### about the type: type = note.getElementsByTagName('type')[0]
        if (note.getElementsByTagName('type')): 
            type = note.getElementsByTagName('type')[0]
            type_data = type.childNodes[0].data

        ### about the pitch and octave
        if (note.getElementsByTagName('pitch')):
            pitch = note.getElementsByTagName('pitch')[0]

            step = pitch.getElementsByTagName('step')[0]
            octave = pitch.getElementsByTagName('octave')[0]

            #if (step.childNodes):
            step_data = step.childNodes[0].data
            
            #if (octave.childNodes):
            octave_data = octave.childNodes[0].data

            if(pitch.getElementsByTagName('alter')):
                alter = pitch.getElementsByTagName('alter')[0]
                alter_data = alter.childNodes[0].data
                # print(alter.childNodes[0].data)

        if (step_data == ''):
            step_data = '[ ]'
            pre_step_data = pre_x_1 = pre_x_2 = ''

        if (type_data == ''):
            type_data = '---'

        ### to reguar the right-hand or left-hand
        if (note.getElementsByTagName('staff')):
            hand = 2
            staff = note.getElementsByTagName('staff')[0]
            staff_data = staff.childNodes[0].data           
            # flag_of_daul to 0
            flag_of_daul = 0

            ### dual(int(staff_data),pre_staff)
            if(note.hasAttribute('default-x')):
                #if(int(staff_data) == pre_staff):
                now_x = note.getAttribute('default-x')
                
                ### when daul very close 
                if(int(staff_data)==1):
                    if(pre_x_1 != ''):
                        pre_x_1_flaot = float(pre_x_1)
                        if(now_x != ''):
                            now_x_float = float(now_x)
                            close_daul = math.fabs(pre_x_1_flaot-now_x_float)

                    #if(pre_x_1==now_x):
                    if(close_daul < 30):
                        if(pre_x_1 != ''):
                            daul = 'there is a right daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
                            flag_of_daul = 1
                            # simple_daul(pre_step_data, pre_octave_data, step_data, octave_data)
                
                if(int(staff_data)==2):
                    if(pre_x_2 != ''):
                        pre_x_2_flaot = float(pre_x_2)
                        if(now_x != ''):
                            now_x_float = float(now_x)
                            close_daul = math.fabs(pre_x_2_flaot-now_x_float)

                    if(close_daul < 30):
                        if(pre_x_2 != ''):
                    # if(pre_x_2==now_x):
                    #if(b <= 30):
                        #print('there is a left daul: ', pre_step_data+pre_octave_data, 'and',step_data+octave_data)
                            daul = 'there is a left daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
                            flag_of_daul = 1
                            # simple_daul(pre_step_data, pre_octave_data, step_data, octave_data)

            # next measure
            if (int(staff_data)== 1):
                if(pre_staff == 2): 
                    # print('pre_staff == 2 and staff_data == 1')
                    #print(measure)
                    timing = 0
                    measure = measure+1
                    print(measure,'=======================================================================')
                    pre_staff = 1
                    pre_step_data = pre_x_1 = pre_x_2 = ''
                    

            if(int(staff_data)== 1):    
                pre_staff = 1
                pre_x_1 = note.getAttribute('default-x')
                pre_step_data = step_data
                pre_octave_data = octave_data
                # print(staff_data_1_x)
                    ### test!
                

            if(int(staff_data)== 2):
                pre_staff = 2   
                pre_x_2 = note.getAttribute('default-x')
                pre_step_data = step_data
                pre_octave_data = octave_data
                # print(staff_data_2_x)
            
            if(timing > int(beats)):
                timing = 0  

        ### one-hand for measure and daul 
        if (hand == 1): 
            single_flag_of_daul = 0

            if(note.hasAttribute('default-x')):
                single_now_x = note.getAttribute('default-x')
                if(single_pre_x != ''):
                    single_pre_x_flaot = float(single_pre_x)
                    if(single_now_x != ''):
                        single_now_x_float = float(single_now_x)
                        close_daul = math.fabs(single_pre_x_flaot-single_now_x_float)

                    if(close_daul < 30):
                        if(single_pre_x != ''):
                            daul='there is a daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
                            single_flag_of_daul = 1

            pre_step_data = step_data
            pre_octave_data = octave_data

            single_pre_x = single_now_x
            #print(single_time,timing)
            
            if (single_flag_of_daul == 0):
                single_time += float(rhythm)

            if (single_time > int(beats)):
                single_measure += 1
                print(single_measure,'----------------------------------------------------------------------')
                single_time = 0
                single_time += float(rhythm)
                timing = 0
                single_pre_x = ''

            timing = single_time


        if (staff_data == ''):
            staff_data = '0'

        # about the timing
        if(flag_of_daul == 0 and (hand != 1)):
            timing += float(rhythm)

        ### About the PI        
        PI = math.floor(timing - float(rhythm) +1)
        
        # about the ID : note num(4) // measure(2) // staff(1) // timing(1)
        # ID: note_num 
        note_num = str(note_num).zfill(4)
        
        # ID: measure_id
        measure_id = str(measure) 
        measure_id = measure_id.zfill(2)
        # ID: measure_id of one-hand
        if staff_data == '0':
            measure_id = str(single_measure)
            measure_id = measure_id.zfill(2)

        # ID: staff_id
        staff_id = staff_data

        # ID = note_num + measure_id + staff_id + str(PI)
        
        print(str(PI)+'  '+
            step_data
            +octave_data
            +'  '+alter_data
            +'\t\t'+type_data
            +'\t\t'+staff_data
            +'\t\t'+rhythm)
        

        # for_sheet.create_sheet()

        ### for draw the notes!!!!!
        # print(str(measure) + staff_data + str(PI) + type_data)
        for_sheet.create_notes(type_data)

        if (daul != ''):
            print(daul)

        ### mini_rhythm
        if(float(rhythm) < float(mini_rhythm)):
            mini_rhythm = rhythm

        ### max_measure
        if(int(measure) > int(max_measure)):
            max_measure = measure

    print('mini rhythm is : ',mini_rhythm)
    # print(max_measure)
