### import parse
from xml.dom.minidom import parse
import xml.dom.minidom
from xml.etree.ElementTree import ElementTree, Element, parse

### import math
import math

### import file from for_parsing, for_sheet
import for_parsing
import for_sheet

### global note_x : all the notes x location
global note_x
note_x = []

### all the notes' MIDI key, x, y
MIDI_str = []
key_x_str = []
key_y_str = []

### def function read_xml
def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

### def funtion write_xml
def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

### def function when change_Tonation then change_notes
def change_Tona_change_notes(filename,add_key):

    ######
    # <step>F</step>
    # <alter>1</alter>
    # <octave>4</octave>
    ######
    
    ### parsing the change-temp
    tree = parse('change-temp.xml')
    root = tree.getroot()

    '''
    find all the measure -> note 
    -> pitch -> step -> octave -> alrer
    count the key of MIDI code

    and then change the new MIDI to new pitch
    ''' 
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for pitch in note.iter('pitch'):
                alter_nun = 0
                for step in pitch.iter('step'):
                    # print('step: ',step.text)
                    step_text = step.text
                for octave in pitch.iter('octave'):
                    # print('octave: ',octave.text)
                    octave_text = octave.text
                
                if(pitch.iter('alter')):
                    for alter in pitch.iter('alter'):
                        alter = alter.text
                        alter_nun = int(alter)

                # print(step_text,octave_text)

                octave_num = (int(octave_text)+1) * 12
                
                if(step_text == 'C'):
                    step_num = 0

                if(step_text == 'D'):
                    step_num = 2

                if(step_text == 'E'):
                    step_num = 4

                if(step_text == 'F'):
                    step_num = 5

                if(step_text == 'G'):
                    step_num = 7

                if(step_text == 'A'):
                    step_num = 9

                if(step_text == 'B'):
                    step_num = 11

                midi = step_num + octave_num + alter_nun
                # print('Midi: ', midi )
                new_midi = midi + add_key
                # print('New Midi: ', new_midi)

                new_octave = (new_midi // 12) -1
                new_step = new_midi % 12

                if(new_step == 0):
                    new_step = 'C'
                if(new_step == 1):
                    new_step = 'C'

                if(new_step == 2):
                    new_step = 'D'
                if(new_step == 3):
                    new_step = 'D'

                if(new_step == 4):
                    new_step = 'E'

                if(new_step == 5):
                    new_step = 'F'
                if(new_step == 6):
                    new_step = 'F'

                if(new_step == 7):
                    new_step = 'G'
                if(new_step == 8):
                    new_step = 'G'
                
                if(new_step == 9):
                    new_step = 'A'
                if(new_step == 10):
                    new_step = 'A'
                
                if(new_step == 11):
                    new_step = 'B'
    
                step.text = ''
                step.text += new_step

                octave.text = ''
                octave.text += str(new_octave)

                # print('new: ',step.text, octave.text)
                
                # write_xml(tree, 'change-key.xml')
                write_xml(tree, 'change-temp.xml')

    # print('  the file "change-key-note" is saved.')    

### def function to change tonation
def change_Tona(filename, Tona ,accent, daul):
    
    ### if daul or accent is changed, then read file named 'change-temp.xml'
    if (accent == 1 or daul == 1): 
        filename = 'change-temp.xml'

    ### parsing the file
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    tree = read_xml(filename)
    
    ### change tonation str
    Tona_str = ''

    ### define the pre tionation num and str
    if(Tona == 'C'):
        Tona_str = '0'
        Tona_num = 60

    if(Tona == 'D'):
        Tona_str = '2'
        Tona_num = 62

    if(Tona == 'E'):
        Tona_str = '4'
        Tona_num = 64

    if(Tona == 'F'):
        Tona_str = '6'
        Tona_num = 65

    if(Tona == 'G'):
        Tona_str = '1'
        Tona_num = 67

    if(Tona == 'A'):
        Tona_str = '3'
        Tona_num = 69

    if(Tona == 'B'):
        Tona_str = '5'
        Tona_num = 71
    
    # modify the attri of Tonality
    for fifths in tree.iter('fifths'):
        pre_key = fifths.text
        
        # change the key
        fifths.text = ''
        fifths.text += Tona_str
        # print("key change : ", fifths.text)
        
        write_xml(tree, 'change-temp.xml')
        # write_xml(tree, 'change-key.xml')
        # print('  the file "change-key.xml" is saved.')

    ### when change key, count how many number would add.
    if(pre_key == '0'):
        add_key = Tona_num - 60

    if(pre_key == '1'):
        add_key = Tona_num - 67

    if(pre_key == '2'):
        add_key = Tona_num - 62

    if(pre_key == '3'):
        add_key = Tona_num - 69

    if(pre_key == '4'):
        add_key = Tona_num - 64

    if(pre_key == '5'):
        add_key = Tona_num - 71

    if(pre_key == '6'):
        add_key = Tona_num - 65

    # if(pre_key == '7'):
    #     add_key = Tona_num - 61

    # print('add_key: ',add_key)
    
    ### call the function to change the notes
    change_Tona_change_notes(filename,add_key)

### def function change the tempo
def change_tempo(filename ,Tem, accent, daul, Tona):

    ### if daul or accent is changed, then read file named 'change-temp.xml'
    if (accent == 1 or daul == 1 or Tona == 1):
        filename = 'change-temp.xml'

    ### global DOMTree, collection, tree
    global DOMTree, collection, tree

    ### read the filename
    tree = read_xml(filename)

    # change the attr - tempo:
    for per_minute in tree.iter('per-minute'):
        per_minute.text = ''
        per_minute.text += Tem
        # print("tempo change 1: ", per_minute.text)

    for sound in tree.iter('sound'):
        #print(sound.attrib)
        sound.set("tempo", Tem)
        # print("tempo change: ", sound.attrib)
        
        write_xml(tree, "change-temp.xml")
        # write_xml(tree, "change-tem.xml")
        # print('  the file "change-tem.xml" is saved.')

### def function about simple daul(chord)
def simple_daul(filename, accent):
    
    ### open the file named 'change-daul.xml'
    # chord_sim = open('change-daul.xml','w')

    ### if accent was changed, the read the file named 'change-temp.xml'
    if (accent == 1): 
        filename = 'change-temp.xml'
    else:
        change_temp = open('change-temp.xml','w')

    ### parsing the file
    tree = parse(filename)
    root = tree.getroot()

    ### define the queue
    queue = []

    ### pre notes
    daul_pre_note = ''
    daul_staff_data = ''

    ### measure -> notes -> chord 
    ### right hand delete chord, left hand delete chord
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            # print('here note: ',note)
            for staff in note.iter('staff'):
                daul_staff_data = staff.text
                # print('daul_staff_data: ',daul_staff_data)
                
            ### must delete notes
            chord = note.find('chord')
            # print('chord text: ',chord)
            # print('-------------------------')

            ### left hand delete 'chord'
            if(chord != None and daul_staff_data == '2'):
                queue.append(note)

            ### right hand delete 'chord'
            if(chord != None and daul_staff_data == '1'):
                queue.append(daul_pre_note)
            
            daul_pre_note = note

            ### print('queue: ',queue)
        for i in queue:
            measure.remove(i)
            # measure.remove(queue.pop(0))
            # print('deleted queue[0]: ',queue)

        queue = []

    ### save the change to 'change-temp.xml' file
    tree.write('change-temp.xml')
    # tree.write('change-daul.xml')
    # print('  the file "change-daul.xml" is saved.')

### simple rhythm 
### is doesn't work now
def simple_rhythm(filename):
    rhythm = open('change-rhythm.xml','w')
    
    tree = parse(filename)
    root = tree.getroot()

    # tree.write('change-rhythm.xml')
    # print('  the file "change-rhythm.xml" is saved.')

### simple accent, change all the type to qauter
def simple_accent(filename, hands):

    ### open the file named change-temp
    change_temp = open('change-temp.xml','w') 

    # change_accent = open('change-accent.xml','w') 

    ### delete notes
    must_delet_note = 0
    ### queue put the delete notes
    queue_must_delet_note = ''

    ### difine mini duration
    mini_duration = 0

    ### parsing the file
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    
    for_parsing.parsing(collection, note_x, MIDI_str, key_x_str, key_y_str, hands)

    ### define measure and pre staff
    pre_staff = 0
    measure = 1
    
    ##########################################
    ##########################################
    ##########################################

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
    for sound in sounds:
        if (sound.hasAttribute('tempo')):
            sound = sound.getAttribute('tempo')
            print('tempo: ',sound)
    

    pre_staff_data = 1
    
    ### print about the pitch type staff rhyth
    print('pitch\ttype\t\tstaff\t\trhythm')
    print('1=======================================================================')
    total_PI = 1

    ### notes is a list
    notes = collection.getElementsByTagName('note')
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
            mini_duration = int(duration.childNodes[0].data)
            # print('mini_duration: ',mini_duration)

        if(timing >= int(beats) and (hand != 1)):
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

        if (staff_data == ''):
            staff_data = '0'

        # about the timing
        if(flag_of_daul == 0 and (hand != 1)):
            timing += float(rhythm)

        ### About the PI        
        PI = math.floor(timing - float(rhythm) +1)
    
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
    
    # accent_sim = open('change-accent.xml','w')
    
    tree = parse(filename)
    root = tree.getroot()
    queue = []

    now_note_num = 0
    next_mutch_note_tag = 0
    
    '''
    measure -> note 
    append the must delete notes to queue
    '''
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

    tree.write('change-temp.xml')
    # tree.write('change-accent.xml')
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
    # tree1.write('change-accent.xml')
    # print('  the file "change-accent.xml" is saved.')

def hand(filename, hand):
    ### if accent was changed, the read the file named 'change-temp.xml'
    change_temp = open('change-temp.xml','w')

    ### parsing the file
    tree = parse(filename)
    root = tree.getroot()

    ### define the queue
    queue = []

    pre_staff = ''

    ### measure -> notes -> chord 
    ### right hand delete chord, left hand delete chord
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            # print('here note: ',note)
            for staff in note.iter('staff'):
                staff_data = staff.text
                
            ### must delete notes
            ### right hand delete staff 2
            if(staff_data != hand):

                queue.append(note)

            pre_staff = staff_data

        for i in queue:
            measure.remove(i)

        queue = []

    ### save the change to 'change-temp.xml' file
    tree.write('change-temp.xml')
    