### import parsing
from xml.dom.minidom import parse
import xml.dom.minidom

### importtk 
import tkinter as tk
from tkinter import *

### import math
import math

### import draw the music sheet
import for_sheet

### total measure
max_measure = 0

### beats 3/4 or 4/4
beats = 0

### note_x : all the notes' x location 
global note_x
note_x = []

'''
def funtion - draw the music sheet
beats, key, sheet x, sheet y

3/4 or 4/4
key 1 or -1 (sharp or flat)
''' 
def create_sheet(beats, key, x, y):

    ### 4/4 
    if (beats == '4'):
        ### sharp
        if(key == 0):
            photo = PhotoImage(file = '4u4 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x ,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 1):
            photo = PhotoImage(file = '4u1 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x ,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 2):
            photo = PhotoImage(file = '4u2 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x ,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 3):
            photo = PhotoImage(file = '4u3 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 4):
            photo = PhotoImage(file = '4u4 new new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 5):
            photo = PhotoImage(file = '4u5 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 6):
            photo = PhotoImage(file = '4u6 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 7):
            photo = PhotoImage(file = '4u7 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        ### flat
        if(key == -1):
            photo = PhotoImage(file = '4d1 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -2):
            photo = PhotoImage(file = '4d2 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -3):
            photo = PhotoImage(file = '4d3 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -4):
            photo = PhotoImage(file = '4d4 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -5):
            photo = PhotoImage(file = '4d5 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -6):
            photo = PhotoImage(file = '4d6 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -7):
            photo = PhotoImage(file = '4d7 new.gif')
            label_sheet = Label(image = photo)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

    ### 3/4
    if(beats == '3'):
        ### sharp
        if(key == 0):
            photo = PhotoImage(file = '3u0 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 1):
            # photo = PhotoImage(file = '3u1 new.gif')
            photo = PhotoImage(file = '3u1 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 2):
            photo = PhotoImage(file = '3u2 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 3):
            photo = PhotoImage(file = '3u3 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 4):
            photo = PhotoImage(file = '3u4 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 5):
            photo = PhotoImage(file = '3u5 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 6):
            photo = PhotoImage(file = '3u6 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == 7):
            photo = PhotoImage(file = '3u7 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        ### flat
        if(key == -1):
            photo = PhotoImage(file = '3d1 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -2):
            photo = PhotoImage(file = '3d2 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -3):
            photo = PhotoImage(file = '3d3 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -4):
            photo = PhotoImage(file = '3d4 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -5):
            photo = PhotoImage(file = '3d5 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -6):
            photo = PhotoImage(file = '3d6 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!

        if(key == -7):
            photo = PhotoImage(file = '3d7 new.gif')
            label_sheet = Label(image = photo)
            #label.grid(row = 3, column = 1, padx = 5, pady = 5)
            label_sheet.place(x=x,y=y)
            label_sheet.image = photo # keep a reference!


### funtion pasing xml file (root, all notes' x location, MIDI, key_x_str, key_y_str)
def parsing(w, collection, note_x, MIDI_str, key_x_str, key_y_str, hands):
    # w.create_line(0, 0, 400, 400)
    # if (hands == 1):
    #     print('wowowowoow')
    
    '''
    count all the notes
    '''
    notes_all = 0
    notes_rest = 0
    notes_whole = 0
    notes_half = 0
    notes_quarter = 0
    notes_eighth = 0
    notes_16th = 0
    notes_notes = 0

    ### measure's tag
    measure_tag = 0

    ### pre staff - right hand or left hand
    pre_staff = 0

    ### measure
    measure = 1
    

    ### pre right hand pre x, left hand pre x, step and octave 
    pre_x_1 = pre_x_2 = ''
    pre_step_data = pre_octave_data = ''

    ### pre staff
    pre_staff_data = 1

    # about the mini_rhythm for the simple
    mini_rhythm = 6

    '''
    ### about the ID
    # ID = ''
    '''

    # about the (time.rhythm / measure)
    timing = 0
    flag_of_daul = 0

    
    ### single
    single_measure = 1
    single_time = 0
    single_pre_x = ''

    single_flag_of_daul = 0
    

    ### hand default is 1, but we need to input the 2 hands xml file
    hand = 1

    ### the number of notes
    note_num = 0

    ### total PI
    total_PI = 1

    '''
    to defind the sheet: key && divs && time
    ### divisions 3/4 or 4/4
    ### key : fifths
    ### time : beats and beattype
    '''
    attrs = collection.getElementsByTagName('attributes')
    
    for attr in attrs:
        divs = collection.getElementsByTagName('divisions')
        for div in divs:
            divisions = div.childNodes[0].data

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
            
            global beats_111
            beats_111 = int(beats)
            
            ### create_sheet
            x = 200
            y = 20
            create_sheet(beats, int(fifths), x, y)
            # w.create_line(0, 0, 400, 400)

    ### about the write tempo
    directions = collection.getElementsByTagName('direction')
    for direction in directions:
        per_minute = collection.getElementsByTagName('per-minute')[0]
        per_minute = per_minute.childNodes[0].data

    ### about the real tempo
    sounds = collection.getElementsByTagName('sound')
    for sound in sounds:
        if (sound.hasAttribute('tempo')):
            sound = sound.getAttribute('tempo')
            print('tempo: ',sound)
 
    ### ### count all_notes
    notes = collection.getElementsByTagName('note')    
    for note in notes:
        notes_all += 1

    ### print about the pitch / type / staff / rhyth / PI
    print('pitch\t\ttype\t\tstaff\t\trhythm\tPI')
    print('1=======================================================================')

    for note in notes:
        ### if note.hasAttribute('default-x'):
        ###    print('default-x: %s' % note.getAttribute('default-x'))
        
        ### count note when for run again
        note_num = int(note_num) + 1

        ### bool : whether the notes are daul?
        is_daul = 0

        ### daul 
        daul = ''
        close_daul = 0

        ### single 
        # single_pre_x =''
        # single_time = 

        ### default str = ''
        pitch = step_data = octave_data = type_data = staff_next_data  = staff_data = alter_data = ''

        ### duration and count the rhythm
        duration = note.getElementsByTagName('duration')[0]
        rhythm = str(float(duration.childNodes[0].data)/float(divisions))
        
        ### about stem : up and down
        if (note.getElementsByTagName('stem')):
            stem = note.getElementsByTagName('stem')[0]
            stem = stem.childNodes[0].data
            # print('stem: ',stem)
        else:
            ### notes are rest
            stem = 0
            
        
        ### single
        if(timing >= int(beats) and (hand != 1)):
            # print('=======================================================================')
            # single_measure += 1
            timing = 0
        

        ### accidental : temporary sharp or flat
        ### if no temporary accidental --> alter = 0
        ### else alter = 50 (it has been changed)
        if (note.getElementsByTagName('accidental')):
            accidental = note.getElementsByTagName('accidental')[0]
            # alter_data = accidental.childNodes[0].data
            alter_data = '0'
        else:
            alter_data = '50'

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

        '''
        rest notes : 
            octave_data = 10, 
            pre_step_data = pre_x_1 = pre_x_2 = ''
            step_data = '[ ]'
            type_data = '---'
        '''
        if (step_data == ''):
            step_data = '[ ]'
            pre_step_data = pre_x_1 = pre_x_2 = ''
            octave_data = 10

        if (type_data == ''):
            type_data = '---'

        ### to reguar the right-hand or left-hand
        # if (note.getElementsByTagName('staff')):
        ### both hands
        if (hands != 1):
            hand = 2
            ### find out the staff
            staff = note.getElementsByTagName('staff')[0]
            staff_data = staff.childNodes[0].data           
            
            # flag_of_daul to 0
            flag_of_daul = 0

            ### next measure
            if (staff_data != pre_staff_data):
                total_PI = 1

            ### staff_data change the pre_staff_data
            pre_staff_data  = staff_data

            ### dual !!! (int(staff_data),pre_staff)
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
                    if(close_daul < 10):
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

                    if(close_daul < 10):
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
                    total_PI = 1
                    
            if(int(staff_data)== 1):    
                pre_staff = 1
                pre_x_1 = note.getAttribute('default-x')
                pre_step_data = step_data
                pre_octave_data = octave_data

            if(int(staff_data)== 2):
                pre_staff = 2   
                pre_x_2 = note.getAttribute('default-x')
                pre_step_data = step_data
                pre_octave_data = octave_data
                # print(staff_data_2_x)
            
            if(timing > int(beats)):
                timing = 0  

        '''single'''
        '''single'''
        ### one-hand for measure and daul 
        if (hands == 1): 
            single_flag_of_daul = 0
            # PI = 1
            
            staff = note.getElementsByTagName('staff')[0]
            staff_data = staff.childNodes[0].data

            if(note.hasAttribute('default-x')):
                single_now_x = note.getAttribute('default-x')
                if(single_pre_x != ''):
                    single_pre_x_flaot = float(single_pre_x)
                    if(single_now_x != ''):
                        single_now_x_float = float(single_now_x)
                        close_daul = math.fabs(single_pre_x_flaot-single_now_x_float)

                    if(close_daul < 10):
                        if(single_pre_x != ''):
                            daul='there is a daul: ' + str(pre_step_data) + str(pre_octave_data) + ' and ' + str(step_data) + str(octave_data)
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
                ### 
                measure = single_measure
                total_PI = 1

            timing = single_time
            # print ('timing: ', timing)
        '''single'''
        '''single'''

        ### staff_data = 0 
        # if (staff_data == ''):
        #     staff_data = '0'

        if (staff_data == ''):
            staff_data = '0'

        # about the timing
        if(flag_of_daul == 0 and (hand != 1) and hands == 0):
            timing += float(rhythm)

        if(single_flag_of_daul == 0 and hands == 1):
            timing += float(rhythm)
            
        ### About the PI        
        PI = math.floor(timing - float(rhythm) +1)

        ### about the ID : note num(4) // measure(2) // staff(1) // timing(1)
        ### ID: note_num 
        # note_num = str(note_num).zfill(4)
        
        ### ID: measure_id
        # measure_id = str(measure) 
        # measure_id = measure_id.zfill(2)
        
        '''
        single
        ### ID: measure_id of one-hand
        if staff_data == '0':
            measure_id = str(single_measure)
            measure_id = measure_id.zfill(2)
        '''

        ### ID: staff_id
        # staff_id = staff_data
        # ID = note_num + measure_id + staff_id + str(PI)
    
        print(step_data
            +str(octave_data)
            +' '+alter_data
            +'\t\t'+type_data
            +'\t\t'+staff_data
            +'\t\t'+rhythm
            +'       '+str(PI))


        ### count parameters of all the notes
        if (step_data == '[ ]'):
            notes_rest += 1
        else:    
            if (type_data == 'whole'):
                notes_whole += 1
            if (type_data == 'half'):
                notes_half += 1
            if (type_data == 'quarter'):
                notes_quarter += 1
            if (type_data == 'eighth'):
                notes_eighth += 1
            if (type_data == '16th'):
                notes_16th += 1

        # print('notes_all, notes_whole, notes_half, notes_quarter, notes_eighth, notes_16th, notes_rest: ',
        #      notes_all   
        #      notes_whole,
        #      notes_half,
        #      notes_quarter,
        #      notes_eighth,
        #      notes_16th, 
        #      notes_rest)

        ### is daul
        if (daul != ''):
            print(daul)
            is_daul = 1

        ### no daul
        if(is_daul == 0):
            total_PI = total_PI
#########
            if(total_PI ==0):
                total_PI = 1
            

        ### is daul and then is_daul_2 = 1
        if (is_daul == 1):
            total_PI = total_PI - float(rhythm)
#########
            if(total_PI ==0):
                total_PI = 1

            is_daul_2 = 1

        ### measure == 5-8 OR measure == 9-12
        if (measure == 5 and measure_tag == 0):
            # note_x = []
            x = 200
            y = 180
            measure_tag = 1
            create_sheet(beats, int(fifths), x, y)

        if(measure == 9):
            measure_tag == 0

        if (measure == 9 and measure_tag == 0):
            # note_x = []
            x = 200
            y = 360
            measure_tag = 1
            create_sheet(beats, int(fifths), x, y)
        
        if (total_PI >= (int(beats)+1)):
            total_PI = float(total_PI) - float(rhythm)

        ### call the function create_notes from the outside for_sheet
        # print('measure: ', measure)
        for_sheet.create_notes(w, int(measure), float(total_PI), int(staff_data), type_data, step_data, float(rhythm), int(octave_data), int(alter_data), beats_111, note_x, stem, MIDI_str, key_x_str, key_y_str)
        print('total_PI: ',total_PI)
        if (total_PI < int(beats)+1):
            total_PI = total_PI + float(rhythm)

        if(total_PI > int(beats)+1): 
            total_PI = 1

        ### mini_rhythm
        if(float(rhythm) < float(mini_rhythm)):
            mini_rhythm = rhythm

        ### max_measure
        #if(int(measure) > int(max_measure)):
        #    max_measure = measure
            # print('max_measure:' ,max_measure)

        # create_sheet(beats, int(fifths), x, y)
        # w.create_line(0, 0, 400, 400)
        
    print('mini rhythm is : ',mini_rhythm)
    # print('max_measure: ',max_measure)
    
    '''
    if (4 < max_measure  and max_measure < 8):
        x = 200
        y = 180
        create_sheet(beats, int(fifths), x, y)
    
    if (9 < max_measure  and max_measure < 12):
        x = 200
        y = 360
        create_sheet(beats, int(fifths), x, y)
    '''

    print()
    print()
    print()
    print('//////////////////////////////////////////////////////////////')
    print()
    print()
    print()

    '''
    ### kind of all the notes 
    notes_notes = notes_all - notes_rest
    print('notes_all, notes_notes, notes_whole, notes_half, notes_quarter, notes_eighth, notes_16th, notes_rest: ',
            notes_all ,
            notes_notes,  
            notes_whole,
            notes_half,
            notes_quarter,
            notes_eighth,
            notes_16th, 
            notes_rest)
    '''
    
    '''
    ### notes 1u3xu4
    # print(format(0.5236, '.2%'))
    print('notes_whole', format((notes_whole / notes_all), '.2%'))
    print('notes_half', format((notes_half / notes_all), '.2%'))
    print('notes_quarter', format((notes_quarter / notes_all), '.2%'))
    print('notes_eighth', format((notes_eighth / notes_all), '.2%'))
    print('notes_16th', format((notes_16th / notes_all), '.2%'))
    print('notes_notes', format((notes_rest / notes_all), '.2%'))
    print('notes_rest', format((notes_rest / notes_all), '.2%'))
    '''

    ### return fifths and per_minute
    return(fifths, per_minute)
