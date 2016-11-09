### import parsing
from xml.dom.minidom import parse
import xml.dom.minidom

### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse

### import math
import math




def add_node_total_PI(DOMTree, note_num_total_PI, total_PI):
    newEle = DOMTree.createElement("TotalPI")
    newText = DOMTree.createTextNode(str(total_PI))
    newEle.appendChild(newText)

    DOMTree.getElementsByTagName("note")[note_num_total_PI].appendChild(newEle)
    DOMTree.toxml()

    file = open("change-parse.xml", 'w')
    file.write(DOMTree.toxml())

def add_node_rhythm(DOMTree, note_num_total_PI, rhythm):
    newEle = DOMTree.createElement("rhythm")
    newText = DOMTree.createTextNode(str(rhythm))
    newEle.appendChild(newText)

    DOMTree.getElementsByTagName("note")[note_num_total_PI].appendChild(newEle)
    DOMTree.toxml()

    file = open("change-parse.xml", 'w')
    file.write(DOMTree.toxml())

### ### function about melody pitch
def melody_pitch_func(step_data, octave_data, alter_data, staff_data, melody_pitch_temp_R, melody_pitch_temp_L, note_num_total_PI):
    # print(step_data, octave_data, alter_data)
    dict = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    # print("C: ", dict['C'])
    # print('step: ', dict[step_data])

    midi = (int(octave_data)+1) * 12  + dict[step_data] 
    
    if(alter_data == 'natural'):
        midi = midi

    elif(int(alter_data) == 1):
        midi = midi + 1

    elif(int(alter_data) == -1):
        midi = midi - 1

    if(staff_data == '1'):
        melody_pitch_temp_R.append(midi)
    elif(staff_data == '2'):
        melody_pitch_temp_L.append(midi)
    
    # print('pitch_temp_R: ', melody_pitch_temp_R)
    # print('pitch_temp_L: ', melody_pitch_temp_L)

    # print('midi: ', midi)

    ### add_node_MIDI
    newEle = DOMTree.createElement("MIDI")
    newText = DOMTree.createTextNode(str(midi))
    newEle.appendChild(newText)

    DOMTree.getElementsByTagName("note")[note_num_total_PI].appendChild(newEle)
    DOMTree.toxml()

    file = open("change-parse.xml", 'w')
    file.write(DOMTree.toxml())


def parsing(DOMTree, collection, hands):

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

    notes_all = 0

    ### total PI
    total_PI = 1
    note_num_total_PI = 0

    melody_pitch_temp_R = []
    melody_pitch_temp_L = []
    
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
    print('pitch\t\ttype\t\tstaff\t\trhythm\t\tPI')
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
            alter_data = accidental.childNodes[0].data
            # print(?'haaaaa' , alter_data)
            # alter_data = '1'

            if(alter_data == 'natural'):
                # print('     is natural')
                alter_data = alter_data
            
        else:
            alter_data = '5'
            

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
                # print('alter_data: ',alter_data)

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
            octave_data = 9

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

            else:
                single_now_x = ''


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

        ### $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ####
        print(step_data
            +str(octave_data)
            +' '+alter_data
            +'\t\t'+type_data
            +'\t\t'+staff_data
            +'\t\t'+rhythm
            +'        '+str(PI))
        
        ### rhythm
        add_node_rhythm(DOMTree, note_num_total_PI, rhythm)

        ### MIDI
        if(step_data != '[ ]'):
            melody_pitch_func(step_data, str(octave_data), alter_data, staff_data, melody_pitch_temp_R, melody_pitch_temp_L, note_num_total_PI)



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

        
        if (total_PI >= (int(beats)+1)):
            total_PI = float(total_PI) - float(rhythm)
        
        # print('total_PI: ',total_PI)

        ### add_node about total_PI !!!
        add_node_total_PI(DOMTree, note_num_total_PI, total_PI)

        total_PI = float(total_PI)
        note_num_total_PI = note_num_total_PI + 1
        # print('note_num: ',note_num_total_PI)


        if (total_PI < int(beats)+1):
            total_PI = total_PI + float(rhythm)

        if(total_PI > int(beats)+1): 
            total_PI = 1

        ### mini_rhythm
        if(float(rhythm) < float(mini_rhythm)):
            mini_rhythm = rhythm

        # ### max_measure
        # if(int(measure) > int(max_measure)):
        #     max_measure = measure
        #     print('max_measure:' ,max_measure)
        
    print('mini rhythm is : ',mini_rhythm)
    # print('max_measure: ',max_measure)

    print()
    print()
    print()
    print('//////////////////////////////////////////////////////////////')
    print()
    print()
    print()
   
DOMTree = xml.dom.minidom.parse('sonatina2.xml')
collection = DOMTree.documentElement

hands = 0
parsing(DOMTree, collection, hands)

