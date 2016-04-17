from xml.dom.minidom import parse
import xml.dom.minidom
import math

from xml.etree.ElementTree import ElementTree,Element

beats = 0


def direction(directions):
     for direction in directions:
        per_minute = collection.getElementsByTagName('per-minute')[0]
        per_minute = per_minute.childNodes[0].data
        # print('view_tempo: ',per_minute)

def sound(sounds):
    for sound in sounds:
        if (sound.hasAttribute('tempo')):
            sound = sound.getAttribute('tempo')
            print('tempo: ',sound)

### funtion pasing xml file
def parsing(collection):
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
            #print(beats)
        
        if ((int(beats) == 6) and (int(beattype) ==8)):
            beats = 3
            return(beats)

    ### about the tempo
    directions = collection.getElementsByTagName('direction')
    direction(directions)

    sounds = collection.getElementsByTagName('sound')
    sound(sounds)
    # print(sounds)
    
    ##################################################
    ### if no set tempo ! add new node about tempo !!!
    #if (sounds == []):
     #   add_tempo_node()
#

    pre_staff_data = 1

    ### print about the pitch type staff rhyth
    print('pitch\t\ttype\t\tstaff\t\trhythm')
    total_PI = 1
    ### notes is a list
    notes = collection.getElementsByTagName('note')
    print('1=======================================================================')

    for note in notes:
        # if note.hasAttribute('default-x'):
        #   print('default-x: %s' % note.getAttribute('default-x'))
        note_num = int(note_num) + 1
        
        is_daul = 0
        
        daul = ''
        close_daul = 0

        pitch = step_data = octave_data = type_data = staff_next_data  = staff_data = alter_data = ''

        duration = note.getElementsByTagName('duration')[0]
        rhythm = str(float(duration.childNodes[0].data)/float(divisions))
        
        if(timing >= int(beats) and (hand != 1)):
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
                    if(close_daul < 30):
                        if(pre_x_1 != ''):
                            daul = 'there is a right daul: '+pre_step_data+pre_octave_data+' and '+step_data+octave_data
                            flag_of_daul = 1
                            # simple_daul(pre_step_data, pre_octave_data, step_data, octave_data)
                            #is_daul = 1

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
                            #is_daul = 1

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
            staff_data = '1'

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
            +octave_data
            +'  '+alter_data
            +'\t\t'+type_data
            +'\t\t'+staff_data
            +'\t\t'+rhythm)
        
        if (daul != ''):
            print(daul)
            is_daul = 1

        if(is_daul == 0):
            print ('total_PI: ', float(total_PI))

        if (is_daul == 1):
            total_PI = total_PI - float(rhythm)
            print ('total_PI: ', total_PI)
            is_daul_2 = 1

        if (total_PI < int(beats)+1):
            total_PI = total_PI + float(rhythm)

        if(total_PI > int(beats)+1): 
            total_PI = 1

        if(float(rhythm) < float(mini_rhythm)):
            mini_rhythm = rhythm


    print('mini rhythm is : ',mini_rhythm)


### funtion read xml file
def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

### find the node path
def change_tempo(beats):
    # 屬性修改 - tempo:
    new_tempo = input('What tempo you want? ')
    
    for per_minute in tree.iter('per-minute'):
        # print(per_minute.text)
        per_minute.text = ''
        per_minute.text += new_tempo
        

    for sound in tree.iter('sound'):
        if(beats == 3):
            new_tempo = float(new_tempo)
            new_tempo = new_tempo + new_tempo / 2
            # print(new_tempo)
            new_tempo = str(new_tempo)
        #print(sound.attrib)
        sound.set("tempo", new_tempo)
        #print(sound.attrib)



def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)


if __name__ == "__main__":
    
    ### read xml file 
    DOMTree = xml.dom.minidom.parse('two-hand-5.xml')
    ### collection is the tree
    collection = DOMTree.documentElement
    ### minidom = pasring the xml file , collection is the tree
    beats = parsing(collection)

    ### about ElementTree and simplize
    tree = read_xml("two-hand-5.xml")
    
    # change tempo
    change_tempo(beats)


    ### write the xml file 
    write_xml(tree, "simple.xml")
    print('  the file "simple.xml" is saved.')


