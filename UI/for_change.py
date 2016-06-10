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


from xml.etree.ElementTree import ElementTree, Element
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

import buttom_Play
# import mtTkinter as Tkinter
# from mtTkinter import *
# import mtTkinter as Tkinter

import math

global note_x
note_x = []

global w

import for_change
import untitled


def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)


def change_temp(filename, daul, rhythm, accent, Default_Tona, Tona, Tem):
    # print(daul, rhythm, accent, Mode, Tona, Tem)

    if (accent == 1):
        change_temp = open('change-temp.xml','w')

        must_delet_note = 0
        queue_must_delet_note = ''

        mini_duration = 0

        ##########################################
        ##########################################
        ##########################################
        DOMTree = xml.dom.minidom.parse(filename)
        collection = DOMTree.documentElement
        for_parsing.parsing(collection, note_x)

        pre_staff = 0
        measure = 1
        
        pre_x_1 = pre_x_2 = ''
        pre_step_data = pre_octave_data = ''

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
        pre_staff_data = 1
        
        ### print about the pitch type staff rhyth
        print('pitch\ttype\t\tstaff\t\trhythm')
        total_PI = 1

        ### notes is a list
        notes = collection.getElementsByTagName('note')
        print('1=======================================================================')

        for note in notes:

            # print('!!!!!!!!!! note: ',note)
            # if note.hasAttribute('default-x'):
            #   print('default-x: %s' % note.getAttribute('default-x'))
            note_num = int(note_num) + 1

            is_daul = 0

            daul = ''
            close_daul = 0

            pitch = step_data = octave_data = type_data = staff_next_data  = staff_data = alter_data = ''

            duration = note.getElementsByTagName('duration')[0]
            rhythm = str(float(duration.childNodes[0].data)/float(divisions))

            rhythm_1 = float(rhythm)
            
            if (rhythm_1 == 1.0):
                # print('rhythm: ',rhythm_1)
                mini_duration = int(duration.childNodes[0].data)
                # print('mini_duration: ',mini_duration)

            if(timing >= int(beats) and (hand != 1)):
                # print('=======================================================================')
                # single_measure += 1
                timing = 0

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

            if (step_data == ''):
                step_data = '[ ]'
                pre_step_data = pre_x_1 = pre_x_2 = ''
                octave_data = 10

            if (type_data == ''):
                type_data = '---'

            ### to reguar the right-hand or left-hand
            if (note.getElementsByTagName('staff')):
                hand = 2
                staff = note.getElementsByTagName('staff')[0]
                staff_data = staff.childNodes[0].data           
                # flag_of_daul to 0
                flag_of_daul = 0

                if (staff_data != pre_staff_data):
                    total_PI = 1

                pre_staff_data  = staff_data

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

                        if(close_daul < 20):
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
        
            print(step_data
                +str(octave_data)
                +' '+alter_data
                +'\t\t'+type_data
                +'\t\t'+staff_data
                +'\t\t'+rhythm
                +'       '+str(PI))


            if (daul != ''):
                print(daul)
                is_daul = 1

            if(is_daul == 0):
                # print ('total_PI: ', float(total_PI))
                total_PI = total_PI

            if (is_daul == 1):
                total_PI = total_PI - float(rhythm)
                # print ('total_PI: ', total_PI)
                is_daul_2 = 1


            # print('total_PI: ',total_PI)

            # ---------------------------- # 
            if(total_PI != int(total_PI)):
                # print('here must stay!!!')
                queue_must_delet_note = queue_must_delet_note + str(must_delet_note) +' '
            # ---------------------------- #

            if (total_PI < int(beats)+1):
                total_PI = total_PI + float(rhythm)

            if(total_PI > int(beats)+1): 
                total_PI = 1

            must_delet_note += 1

        ##########################################
        ##########################################
        ##########################################


        ### remove the notes! 
        # print('queue_must_delet_note: ',queue_must_delet_note)
        queue_must_delet_note = queue_must_delet_note.split(' ')
        # print(queue_must_delet_note)
        # print('len: ',len(queue_must_delet_note))
        
        accent_sim = open('change-accent.xml','w')
        
        tree = parse(filename)
        root = tree.getroot()
        queue = []

        now_note_num = 0
        next_mutch_note_tag = 0
        
        for measure in root.iter('measure'):
            for note1 in measure.iter('note'): 
                # print(note1)
                if(now_note_num == int(queue_must_delet_note[next_mutch_note_tag])):
                    # print('delete!!!!!!')
                    queue.append(note1)

                    ### next mutch note_num
                    next_mutch_note_tag += 1
                    
                    # print('next_mutch_note_tag: ',next_mutch_note_tag)
                    if(next_mutch_note_tag == len(queue_must_delet_note)-1):
                        next_mutch_note_tag = 0
                        # print('-------- next_mutch_note_tag: ',next_mutch_note_tag)
                    
                now_note_num += 1
                # print('now_note_num: ',now_note_num)

            for i in queue:
                measure.remove(i)

            queue = []

        tree.write('change-accent.xml')
        # print('  the file "change-accent.xml" is saved.')

        ### modify duration if(duration < mini_duration) and type change
        tree1 = read_xml('change-temp.xml')

        for duration in tree1.iter('duration'):
            if(int(duration.text) < mini_duration):
                duration.text = ''
                duration.text += str(mini_duration)
                # print('duration had been change !!!!')
        
        for type in tree1.iter('type'):
            if( type.text != 'quarter' and type.text != 'half' and type.text != 'whole'):
                type.text = ''
                type.text += 'quarter'
                print('type had been change !!!!')
        
        tree1.write('change-temp.xml')


    ### daul
    if (daul == 1):

        change_temp = open('change-temp.xml','w')
        
        tree = parse(filename)
        root = tree.getroot()

        queue = []

        for measure in root.iter('measure'):
            for note in measure.iter('note'):
                ### 要刪除的音
                chord =  note.find('chord')
                
                if(chord != None):
                    queue.append(note)
            # print('queue: ',queue)
            
            for i in queue:
                measure.remove(i)
                # measure.remove(queue.pop(0))
                # print('deleted queue[0]: ',queue)

            queue = []

        tree.write('change-temp.xml')



    
    if (Tona != Default_Tona):
        print('change Tona')

    # if (Tem == ):











