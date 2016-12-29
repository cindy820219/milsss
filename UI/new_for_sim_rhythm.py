### import parsing
from xml.dom.minidom import parse
import xml.dom.minidom

### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse

### import math
import math


### if it's cut note, change melody_cutnote[] of staff_data
def melody_cut_note(melody_cutnote, measure, staff_data):
    if(len(melody_cutnote) < measure) :
        melody_cutnote.append(staff_data)
        # print(melody_cutnote)    

### count right hand and left hand rhythm of a measure 
def melody_rhythm_count(staff_data, rhythm, melody_rhythm_R, melody_rhythm_L):    
    if(rhythm == '0.25'):
        if(staff_data == '1'):
            melody_rhythm_R[0] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[0] = 1

    if(rhythm == '0.5'):
        if(staff_data == '1'):
            melody_rhythm_R[1] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[1] = 1

    if(rhythm == '0.75'):
        if(staff_data == '1'):
            melody_rhythm_R[2] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[2] = 1

    if(rhythm == '1' or rhythm == '1.0'):
        if(staff_data == '1'):
            melody_rhythm_R[3] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[3] = 1

    if(rhythm == '1.25'):
        if(staff_data == '1'):
            melody_rhythm_R[4] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[4] = 1

    if(rhythm == '1.5'):
        if(staff_data == '1'):
            melody_rhythm_R[5] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[5] = 1

    if(rhythm == '1.75'):
        if(staff_data == '1'):
            melody_rhythm_R[6] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[6] = 1

    if(rhythm == '2' or rhythm == '2.0'):
        if(staff_data == '1'):
            melody_rhythm_R[7] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[7] = 1

    if(rhythm == '2.25'):
        if(staff_data == '1'):
            melody_rhythm_R[8] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[8] = 1

    if(rhythm == '2.5'):
        if(staff_data == '1'):
            melody_rhythm_R[9] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[9] = 1

    if(rhythm == '2.75'):
        if(staff_data == '1'):
            melody_rhythm_R[10] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[10] = 1

    if(rhythm == '3' or rhythm == '3.0'):
        if(staff_data == '1'):
            melody_rhythm_R[11] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[11] = 1

    if(rhythm == '3.25'):
        if(staff_data == '1'):
            melody_rhythm_R[12] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[12] = 1

    if(rhythm == '3.5'):
        if(staff_data == '1'):
            melody_rhythm_R[13] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[13] = 1

    if(rhythm == '3.75'):
        if(staff_data == '1'):
            melody_rhythm_R[14] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[14] = 1

    if(rhythm == '4.0' or rhythm == '4'):
        if(staff_data == '1'):
            melody_rhythm_R[15] = 1
        elif(staff_data == '2'):
            melody_rhythm_L[15] = 1
            
    # print('melody_rhythm_R: ',melody_rhythm_R)
    # print('melody_rhythm_L: ',melody_rhythm_L)

### function about melody rhythm
def melody_rhythm_func(melody_rhythm, melody_rhythm_R, melody_rhythm_L):
    # print('R: ', melody_rhythm_R)
    # print('L: ', melody_rhythm_L)

    # print('find: ',melody_rhythm_R.index(1))
    # print('find: ',melody_rhythm_L.index(1))

    ### maxi sum is 15 !
    sum_R = sum(melody_rhythm_R)
    sum_L = sum(melody_rhythm_L)

    ### if sum_R > sum_L
    if(sum_R >= sum_L): 
        melody_rhythm.append('1')

    elif(sum_R < sum_L): 
        melody_rhythm.append('2')

    # elif(sum_R == sum_L): 
    #     ### index 
        # print('ggggggggggggggggggggggggggg')
        # print(melody_rhythm_R.index(1))
        # print(melody_rhythm_L.index(1))
        if(melody_rhythm_L.index(1) == True):
            print('aaa')
            # melody_rhythm.append('1')
        else:
            if(melody_rhythm_R.index(1) < melody_rhythm_L.index(1)):
                melody_rhythm.append('1')
            elif(melody_rhythm_R.index(1) > melody_rhythm_L.index(1)):
                melody_rhythm.append('2')
            elif(melody_rhythm_R.index(1) == melody_rhythm_L.index(1)):
                melody_rhythm.append('1')

    # print('melody_rhythm: ', melody_rhythm)
    return(melody_rhythm)

### ### function about melody pitch
def melody_pitch_func(DOMTree, collection, step_data, octave_data, alter_data, staff_data, melody_pitch_temp_R, melody_pitch_temp_L, note_num_total_PI):
        

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

    file = open("change_temp.xml", 'w')
    file.write(DOMTree.toxml())

### function about melody_pitch
def melody_pitch_set_func(melody_pitch, melody_pitch_temp_R, melody_pitch_temp_L):
    len_R = len(list(set(melody_pitch_temp_R)))
    len_L = len(list(set(melody_pitch_temp_L)))

    if(len_R > len_L):
        melody_pitch.append('1')

    if(len_R < len_L):
        melody_pitch.append('2')

    if(len_R == len_L):
        melody_pitch.append('1')

    # print('melody_pitch:  ', melody_pitch)
    return(melody_pitch)

### funtion pasing xml file (root, all notes' x location, MIDI, key_x_str, key_y_str)

### add node about total PI
def add_node_total_PI(DOMTree, note_num_total_PI, total_PI):
    newEle = DOMTree.createElement("TotalPI")
    newText = DOMTree.createTextNode(str(total_PI))
    newEle.appendChild(newText)

    DOMTree.getElementsByTagName("note")[note_num_total_PI].appendChild(newEle)
    DOMTree.toxml()

    file = open("change_temp.xml", 'w')
    file.write(DOMTree.toxml())

### add node about rhythm
def add_node_rhythm(DOMTree, note_num_total_PI, rhythm):
    newEle = DOMTree.createElement("rhythm")
    newText = DOMTree.createTextNode(str(rhythm))
    newEle.appendChild(newText)

    DOMTree.getElementsByTagName("note")[note_num_total_PI].appendChild(newEle)
    DOMTree.toxml()

    file = open("change_temp.xml", 'w')
    file.write(DOMTree.toxml())

def Melody_func(Melody, melody_cutnote, melody_rhythm, melody_pitch):
    ### measure !

    print('melody_cutnote', melody_cutnote)
    print('melody_rhythm ', melody_rhythm)
    print('melody_pitch  ', melody_pitch)

    length = len(melody_pitch)
    # print('length: ',length)
    if(melody_rhythm[length-1] == melody_pitch[length-1]):
        # print('same', melody_rhythm[length-1])
        Melody.append(melody_rhythm[length-1])

    elif(melody_rhythm[length-1] != melody_pitch[length-1] ):
        # print('diff: ', melody_rhythm[length-1], melody_pitch[length-1])
        # Melody.append('D')
        ### melody_rhythm = melody_cutnote ---> melody_rhythm
        if(melody_rhythm[length-1] == melody_cutnote[length-1]):
            Melody.append(melody_rhythm[length-1])
            print('a')
        ### melody_pitch = melody_cutnote ---> melody_pitch
        elif(melody_pitch[length-1] == melody_cutnote[length-1]):
            Melody.append(melody_pitch[length-1])
            print('b')
        ### melody_cutnote == 0 ---> '1'
        elif(melody_cutnote[length-1] == '0'):
            Melody.append('1')
            print('c')

def add_Melody_node_func(DOMTree, Melody, level):
    # print(Melody)
    tree = parse('change_temp.xml')
    root = tree.getroot()

    # print('reverse', reMelody)

    for measure in root.iter('measure'):
        Main = Melody.pop(0)
        
        for note in measure.iter('note'):
            for staff in note.iter('staff'):
                    staff_text = staff.text
                    if(Main == staff_text):
                        xml.etree.ElementTree.SubElement(note, 'melody')
                        note.find('melody').text = 'main'
                    else:
                        xml.etree.ElementTree.SubElement(note, 'melody')
                        note.find('melody').text = 'no_main'

    tree.write('change_rhythm.xml')
    
    if(level == 2):
        high_melody()
    if(level == 1):
        low_melody()

def high_melody():
    print('high')

    tree = parse('change_rhythm.xml')
    root = tree.getroot()

    for beats in root.iter('beats'):
        print('' )
        print('' )
        print('' )
        print('' )
        beat_t = beats.text
        print('!!!!!!!!!! beats;', beats.text)
        print('' )
        print('' )
        print('' )
        print('' )

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for melody in note.iter('melody'):
                melody_text = melody.text
                for TotalPI in note.iter('TotalPI'):
                    TotalPI_text = TotalPI.text
                    break
                if(beat_t != '3'):
                    print(' beats == 4')    
                    # print('melody_text, rhythm_text: ', melody_text, TotalPI_text)
                    if (3.0 > float(TotalPI_text) > 1.0 and melody_text == 'no_main'):
                        xml.etree.ElementTree.SubElement(note, 'rest')
                    if (5.0 > float(TotalPI_text) > 3.0 and melody_text == 'no_main'):
                        xml.etree.ElementTree.SubElement(note, 'rest')

                # if(beat_t == 4):
                #     print(' beats!!! == 4')    
                #     # print('melody_text, rhythm_text: ', melody_text, TotalPI_text)
                #     if (3.0 > float(TotalPI_text) > 1.0 and melody_text == 'no_main'):
                #         xml.etree.ElementTree.SubElement(note, 'rest')
                #     if (5.0 > float(TotalPI_text) > 3.0 and melody_text == 'no_main'):
                #         xml.etree.ElementTree.SubElement(note, 'rest')

                if(beat_t == '3'):
                    print(' beats == 3')    
                    # print('melody_text, rhythm_text: ', melody_text, TotalPI_text)
                    if (float(TotalPI_text) > 1.0 and melody_text == 'no_main'):
                        xml.etree.ElementTree.SubElement(note, 'rest')
                # if(beat_t == 3):
                #     print(' beats == 3')    
                #     # print('melody_text, rhythm_text: ', melody_text, TotalPI_text)
                #     if (float(TotalPI_text) > 1.0 and melody_text == 'no_main'):
                #         xml.etree.ElementTree.SubElement(note, 'rest')
                   
    tree.write('delete_high.xml')
    tree.write('change_temp.xml')
    print(' ---------->  have change high rhythm')
    print('  save the file name "delete_high.xml"')

def low_melody():
    print('low')

    tree = parse('change_rhythm.xml')
    root = tree.getroot()

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for melody in note.iter('melody'):
                melody_text = melody.text
                if(melody_text == 'no_main'):
                    xml.etree.ElementTree.SubElement(note, 'rest')

    tree.write('delete_low.xml')
    tree.write('change_temp.xml')
    print(' ---------->  have change low rhythm')
    print('  save the file name "delete_low.xml"')

def rhythm_parsing(DOMTree, collection, hands, rhythm, level):
    print(' ---------->  in rhythm_parsing funtion')
    # print('level: ',level)

    ### melody define
    melody_cutnote = []
    melody_rhythm  = []
    melody_rhythm_R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    melody_rhythm_L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    sum_R = 0
    sum_L = 0

    melody_pitch  = []
    melody_pitch_temp_R = []
    melody_pitch_temp_L = []

    Melody = []

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
    note_num_total_PI = 0
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

                    ### melody about cut note ! 
                    ### if no cut note, then put '0' in the array melody_cutnote[]
                    if(len(melody_cutnote) < measure) :
                        melody_cutnote.append('0')

                    ### important !!!
                    # print('melody_cutnote:' ,melody_cutnote)

                    ### melody about rhythm and count all the different
                    # print(melody_rhythm_R, '  ', sum(melody_rhythm_R))
                    # print(melody_rhythm_L, '  ', sum(melody_rhythm_L))
                    melody_rhythm = melody_rhythm_func(melody_rhythm, melody_rhythm_R, melody_rhythm_L)
                    ### important !!!
                    # print('melody_rhythm: ', melody_rhythm)
                    ### next measure, need to clear melody_rhythm_R and melody_rhythm_L
                    

                    melody_pitch = melody_pitch_set_func(melody_pitch, melody_pitch_temp_R, melody_pitch_temp_L)
                    ### important !!!
                    # print('melody_pitch:  ', melody_pitch)

                    ### function for the Melody
                    Melody_func(Melody, melody_cutnote, melody_rhythm, melody_pitch)


                    ### clear for the next measure !!
                    melody_rhythm_R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    melody_rhythm_L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                    melody_pitch_temp_R = []
                    melody_pitch_temp_L = []


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
    

        ### $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ ####
        print(step_data
            +str(octave_data)
            +' '+alter_data
            +'\t\t'+type_data
            +'\t\t'+staff_data
            +'\t\t'+rhythm
            +'        '+str(PI))
        
        add_node_rhythm(DOMTree, note_num_total_PI, rhythm)

        ### melody - cut note !!
        if(rhythm =='0.75'):
            melody_cut_note(melody_cutnote, measure, staff_data)
        # print(melody_cutnote)

        ### melody - rhythm !!
        if(step_data != '[ ]'):
            melody_rhythm_count(staff_data, rhythm, melody_rhythm_R, melody_rhythm_L)
        
        ### melody - pitch !!
        if(step_data != '[ ]'):
            melody_pitch_func(DOMTree, collection, step_data, str(octave_data), alter_data, staff_data, melody_pitch_temp_R, melody_pitch_temp_L, note_num_total_PI)


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
    
    
    ### melody 
    

    ###### the final measure !!!
    ### melody cut note
    if(len(melody_cutnote) < measure) :
        melody_cutnote.append('0')
    # print('melody_cutnote:', melody_cutnote)

    ### melody rhythm final measure
    melody_rhythm = melody_rhythm_func(melody_rhythm, melody_rhythm_R, melody_rhythm_L)
    # print('melody_pitch:  ', melody_rhythm)

    ### melody pitch final measure
    melody_pitch = melody_pitch_set_func(melody_pitch, melody_pitch_temp_R, melody_pitch_temp_L)
    # print('melody_pitch:  ', melody_pitch)

    Melody_func(Melody, melody_cutnote, melody_rhythm, melody_pitch)

    print()
    print()
    print()
    print('//////////////////////////////////////////////////////////////')
    print()
    print()
    print()

    # print(Melody)
    add_Melody_node_func(DOMTree, Melody, level)

# DOMTree = xml.dom.minidom.parse('sonatina2.xml')
# collection = DOMTree.documentElement

# rhythm = 1
# hands = 0
# level = 0
# rhythm_parsing(DOMTree, collection, hands, rhythm, level)