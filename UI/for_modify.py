### import parse
from xml.dom.minidom import parse
import xml.dom.minidom
from xml.etree.ElementTree import ElementTree, Element, parse

### import math
import math

### import file from for_parsing, for_sheet
import for_parsing
import for_sheet

### import pprint
import pprint

pp = pprint.PrettyPrinter(indent=4)

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
    
    # print('Tona: ',Tona)
    
    add_key = 0

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
    
    ### print('pre_key: ', pre_key)


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

    ############################
    ############################

    # if(pre_key == '-1'):
    #     add_key = Tona_num - 65

    # if(pre_key == '-2'):
    #     add_key = Tona_num - 70

    # if(pre_key == '-3'):
    #     add_key = Tona_num - 64

    # if(pre_key == '-4'):
    #     add_key = Tona_num - 69

    # if(pre_key == '-5'):
    #     add_key = Tona_num - 72

    # if(pre_key == '-6'):
    #     add_key = Tona_num - 67
    ############################
    ############################
    
    ### add key
    # print('add_key: ', add_key)
    
    # if(pre_key == '7'):
    #     add_key = Tona_num - 61

    # print('add_key: ',add_key)
    
    ### call the function to change the notes
    change_Tona_change_notes(filename, add_key)

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
def simple_daul(filename, accent, level):
    
    ### to count all the chord notes
    chord_num = 0

    ### to count the number of three dual notes
    chord_pre = 0
    chord_now = 0
    chord_three = 0
    
    ### to count the total PI
    total_PI = 1

    ### test !!! not on the on-beat dual notes
    count_rest = 0

    ### open the file named 'change-daul.xml'
    # chord_sim = open('change-daul.xml','w')

    ### hight level = 2, low level = 1
    # print('IN level: ', level)

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
            
            chord_now = 0

            ### must delete notes
            chord = note.find('chord')

            ### count all the chord
            if (chord != None):
                chord_num = chord_num + 1
                chord_now = 1

            ### three notes
            if(chord_pre == 1 and chord_now == 1):
                chord_three = chord_three + 1
     
            # print('chord text: ',chord)
            # print('-------------------------')

            ######### low level #########
            ### left hand delete 'chord'
            if(chord != None and daul_staff_data == '2' and level == '1'):
                queue.append(note)

            ### right hand delete 'chord'
            if(chord != None and daul_staff_data == '1' and level == '1'):
                queue.append(daul_pre_note)
            
            daul_pre_note = note
            ### print('queue: ',queue)
            ######### low level #########


            ######### Original #########
            # ### left hand delete 'chord'
            # if(chord != None and daul_staff_data == '2'):
            #     queue.append(note)

            # ### right hand delete 'chord'
            # if(chord != None and daul_staff_data == '1'):
            #     queue.append(daul_pre_note)
            
            # daul_pre_note = note

            # ### print('queue: ',queue)
            ######### Original #########

            chord_pre = chord_now


        for i in queue:
            measure.remove(i)
            # measure.remove(queue.pop(0))
            # print('deleted queue[0]: ',queue)

        queue = []
    

    ### total chord_num
    # print('chord_num: ',chord_num)
    # print('chord_three: ',chord_three)
    # chord_num = chord_num - chord_three


    ########################### high level ###########################
    ########################### high level ###########################
    ########################### high level ###########################
    if(level == '2'):
        
        ### define all_notes and rest_notes
        all_notes = 0
        rest_notes = 0

        ### count the number of chord we need to keep
        chord_min = chord_num *2 // 5
        chord_max = chord_num *3 // 5
        # print('chord_min: ',chord_min, ', and chord_max: ', chord_max)
        
        queue_0 = []
        queue_1 = []
        queue_3 = []
        queue_2 = []
        queue_4 = []
        queue_delete = []

        ### pre_*
        pre_rhythm = 0
        pre_chord = 0
        pre_total_PI = 1

        ### keep note num
        keep_note_num = 0

        ### to get the divisions :(((
        DOMTree = xml.dom.minidom.parse(filename)
        collection = DOMTree.documentElement

        attrs = collection.getElementsByTagName('attributes')
        for attr in attrs:
            divs = collection.getElementsByTagName('divisions')
            for div in divs:
                divisions = div.childNodes[0].data
            ### print(divisions)

            times = collection.getElementsByTagName('time')
            for time in times:
                beats = time.getElementsByTagName('beats')[0]
                beats = beats.childNodes[0].data


        for measure in root.iter('measure'):
            ### print('----new measure----')

            for note in measure.iter('note'):
                # print('here note: ',note)

                ### count all notes
                # all_notes = all_notes + 1
                
                ### count all rest
                for staff in note.iter('rest'):
                    ### count all notes
                    rest_notes = rest_notes+ 1


                for staff in note.iter('staff'):
                    daul_staff_data = staff.text
                    # print('daul_staff_data: ',daul_staff_data)
                
                for duration in note.iter('duration'):
                    duration_data = duration.text


                ### must delete notes
                chord = note.find('chord')
                
                if (chord == None):
                    total_PI = total_PI + pre_rhythm
                    ### count all notes
                    
                elif (chord != None):
                    all_notes = all_notes + 2


                ### if total_PI >= beats, then turn the total_PI to 1
                if (total_PI >= int(beats)+1):
                    total_PI = 1

                ### print total_PI
                # print ('total_PI: ', total_PI)


                ### now is chord and pre not chord
                if((chord != None and pre_chord == 0)):
                    # total_PI = total_PI - pre_rhythm
                    pre_chord = 1

                    # ### print the total_PI
                    # print ('total_PI: ', total_PI)

                    ### one PI
                    if(1.0 == float(total_PI)):

                        # print(' 1.0 == float(total_PI ')
                        if(daul_staff_data == '2'):
                            # xml.etree.ElementTree.SubElement(note, 'keep', attrib={'keep':'2'})
                            
                            xml.etree.ElementTree.SubElement(note, 'keep')
                            note.find('keep').text = '2'

                            queue_1.append(note)
                            # queue_1.append(daul_staff_data)
                            # print('hahahaha: ', note.find('keep').get('keep'))

                            # queue_1.append(daul_staff_data)
                            # print(note.get('keep'))
                            # keep_note_num = keep_note_num + 1


                        elif (daul_staff_data == '1'):
                            # xml.etree.ElementTree.SubElement(daul_pre_note, 'keep', attrib={'keep':'1'})
                            xml.etree.ElementTree.SubElement(daul_pre_note, 'keep')
                            daul_pre_note.find('keep').text = '1'
                            
                            queue_1.append(daul_pre_note)
                            # queue_1.append(daul_staff_data)
                            # queue_1.append(daul_staff_data)
                            # print(daul_pre_note.get('keep'))
                            # keep_note_num = keep_note_num + 1

                    ### three PI
                    elif(3.0 == float(total_PI)):
                        # print(' 3.0 == float(total_PI ')
                        if(daul_staff_data == '2'):
                            queue_3.append(note)
                            # queue_3.append(daul_staff_data)

                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_3.append(daul_pre_note)
                            # queue_3.append(daul_staff_data)


                            # keep_note_num = keep_note_num + 1

                    ### two PI
                    elif(2.0 == float(total_PI)):
                        # print(' 2.0 == float(total_PI ')
                        if(daul_staff_data == '2'):
                            queue_2.append(note)
                            # queue_2.append(daul_staff_data)
                            
                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_2.append(daul_pre_note)
                            # queue_2.append(daul_staff_data)

                            # keep_note_num = keep_note_num + 1

                    ### four PI
                    elif(4.0 == float(total_PI)):
                        # print(' 4.0 == float(total_PI ')

                        if(daul_staff_data == '2'):
                            queue_4.append(note)
                            # queue_4.append(daul_staff_data)
                            
                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_4.append(daul_pre_note)
                            # queue_4.append(daul_staff_data)

                            # keep_note_num = keep_note_num + 1

                    ### must delet dual note!!! the dual note not on the on-beats!
                    ### must delet dual note!!! the dual note not on the on-beats!
                    ### must delet dual note!!! the dual note not on the on-beats!
                    elif (1<float(total_PI) and float(total_PI)<2):
                        if(daul_staff_data == '2'):
                            queue_delete.append(note)
                            #queue_delete.append(daul_staff_data)
                            
                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_delete.append(daul_pre_note)
                            #queue_delete.append(daul_staff_data)

                    elif (2<float(total_PI) and float(total_PI)<3):
                        if(daul_staff_data == '2'):
                            queue_delete.append(note)
                            #queue_delete.append(daul_staff_data)
                            
                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_delete.append(daul_pre_note)
                            #queue_delete.append(daul_staff_data)

                    elif (3<float(total_PI) and float(total_PI)<4):
                        if(daul_staff_data == '2'):
                            queue_delete.append(note)
                            #queue_delete.append(daul_staff_data)
                            
                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_delete.append(daul_pre_note)
                            # queue_delete.append(daul_staff_data)

                    elif (4<float(total_PI) and float(total_PI)<5):
                        if(daul_staff_data == '2'):
                            queue_delete.append(note)
                            # queue_delete.append(daul_staff_data)
                            
                            # keep_note_num = keep_note_num + 1

                        elif(daul_staff_data == '1'):
                            queue_delete.append(daul_pre_note)
                            # queue_delete.append(daul_staff_data)
                    ### must delet dual note!!! the dual note not on the on-beats!
                    ### must delet dual note!!! the dual note not on the on-beats!
                    ### must delet dual note!!! the dual note not on the on-beats!

                    
                    else:
                        # print('float(total_PI): ', float(total_PI))
                        count_rest = count_rest + 1


                ### now is note chord and pre is chord ###
                elif (chord == None and pre_chord == 1):
                    # total_PI = total_PI + pre_rhythm
                    pre_chord = 0


                    ### print the real total_PI
                    # print ('total_PI: ', total_PI)


                ### now is not chord pre_chord is not
                elif (chord == None and pre_chord == 0):
                    ### print the total_PI
                    # total_PI = total_PI + float(duration_data)/float(divisions)
                    pre_chord = 0

                ### now is chord and pre is chord (three-daul-notes)
                elif (chord != None and pre_chord == 1):
                    ### print the total_PI
                    # print ('total_PI: ', total_PI)

                    queue_0.append(daul_pre_note)
                    pre_chord = 1

                    ### keep the notes ! delete the middle notes
                    # keep_note_num = keep_note_num + 1
                    all_notes = all_notes - 2



                ### mark pre_total_PI 
                pre_total_PI = total_PI
               
                pre_rhythm = float(duration_data)/float(divisions)
                
                daul_pre_note = note


            ### delete all the dual notes not on the on-beat !!!
            ### this is true, but now is test!
            for i in queue_delete:
                measure.remove(i)
            queue_delete = []


            # for j in queue_2:
            #     measure.remove(j)
            # queue_2 = []


        ### count all the on the on-beats dual!!!
        # print('siZe 0: ',len(queue_0))      ### three notes
        # print('siZe 1: ',len(queue_1))      ### PI 1
        # print('siZe 3: ',len(queue_3))      ### PI 3
        # print('siZe 2: ',len(queue_2))      ### PI 2
        # print('siZe 4: ',len(queue_4))      ### PI 4
       
        ### delete note
        # print('siZe delete: ',len(queue_delete))      


        ### count all the notes and not rest notes!!!
        all_notes = all_notes/2
        print('all_chord: ', all_notes)
        # print('rest_notes: ', rest_notes)
        

        ### count the number of 'delete notes'
        mini = all_notes * 2 // 5
        maxi = all_notes * 0.6
        
        if (int(maxi) != maxi) :
            maxi = int(maxi)
            maxi = maxi + 1

        # print('max, min: ', maxi, mini)

        ### #1
        ### mini < len[three] , good !

        if (len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2)+len(queue_4) < mini):
            case = 100

        elif (mini <= len(queue_0)):
            if (len(queue_0) <= maxi):
                case = 1
            elif (len(queue_0) > maxi):
                case = 2

        ### #2  
        ### mini < len[three + 1] , keep three and 1
        elif (mini <= len(queue_0)+len(queue_1)):
            ### good !
            if (len(queue_0)+len(queue_1) <= maxi):
                case = 3

            ### mini < len[three + 1 + 3]   but   maxi < len[three + 1 + 3]
            elif (len(queue_0)+len(queue_1) > maxi):
                case = 4

        ### #3
        ### mini < len[three + 1 + 3] , keep three and 1 ,3
        elif (mini <= len(queue_0)+len(queue_1)+len(queue_3)):
            ### good !
            if (len(queue_0)+len(queue_1)+len(queue_3) <= maxi):
                case = 5

            ### mini < len[three + 1 + 3]   but   maxi < len[three + 1 + 3]
            elif (len(queue_0)+len(queue_1)+len(queue_3) > maxi):
                case = 6

        ### #4
        ### min < [three + 1 + 3 + 2] , keep three and 1,3,2
        elif (mini <= len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2)):
            ### good !
            if (len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2) <= maxi):
                case = 7

            ### mini < len[three + 1 + 3 + 2]   but   maxi < len[three + 1 + 3 + 2]
            elif (mini<len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2)) > maxi:
                case = 8

        ### #5
        ### min < [three + 1 + 3 + 2 + 4] , keep three and 1,3,2,4
        elif (mini <= len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2)+len(queue_4)):
            ### good !
            if (len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2)+len(queue_4) <= maxi):
                case = 9

            ### mini < len[three + 1 + 3 + 2 + 4]   but   maxi < len[three + 1 + 3 + 2 + 4]    
            elif (len(queue_0)+len(queue_1)+len(queue_3)+len(queue_2)+len(queue_4) > maxi):
                case = 10


        
        ###########################################
        # print('case: ', case)

        if(case == 1):
            print('case 1')


        # elif(case == 2):

        elif(case == 3):
            print('case 3')
            # for measureA in root.iter('measure'):
            #     for j in queue_2:
            #         measureA.remove(j)
            #     queue_2 = []

               
        # elif(case == 4):

        # elif(case == 5):

        # elif(case == 6):

        # elif(case == 7):

        # elif(case == 8):

        # elif(case == 9):

        # elif(case == 10):





        # for i in queue:
        #     measure.remove(i)
           

        # note.find('keep').get('keep')
        # print(keep_note_num, ' : break 2')
    # print(keep_note_num, ' : break 3')

    ########################### high level ###########################
    ########################### high level ###########################
    ########################### high level ###########################



    ### save the change to 'change-temp.xml' file
    tree.write('change-temp.xml')

    # tree.write('change-daul.xml')
    # print('  the file "change-daul.xml" is saved.')

### simple rhythm 
### is doesn't work now
def simple_rhythm(filename):
    # rhythm = open('change-rhythm.xml','w')
    
    tree = parse(filename)
    root = tree.getroot()

    # tree.write('change-rhythm.xml')
    # print('  the file "change-rhythm.xml" is saved.')

### simple accent, change all the type to qauter
def simple_accent(w, filename, hands):

    ### open the file named change-temp
    # if (hands == 1):
    #     filename = 'change-temp.xml'
    # else:    
    #     change_temp = open('change-temp.xml','w') 

    ### delete notes
    must_delet_note = 0
    ### queue put the delete notes
    queue_must_delet_note = ''

    ### difine mini duration
    mini_duration = 0

    ### parsing the file
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    
    for_parsing.parsing(w, collection, note_x, MIDI_str, key_x_str, key_y_str, hands)
    
    ### clear all the menu
    w.delete('all')
    
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

def hand(filename, hand,  accent, daul, Tona):
    ### if accent was changed, the read the file named 'change-temp.xml'
    
    ### hand not both, and accent ==0, daul==0, tona ==0
    ### open the file 'change-temp.xml'

    ### else 
    ### filename == 'change-temp.xml'
    if( hand!='0' and accent != 1 and daul != 1 and Tona != 1):
        change_temp = open('change-temp.xml','w')
    else:
        filename = 'change-temp.xml' 

    ### parsing the file
    tree = parse(filename)
    root = tree.getroot()

    ### define the queue
    queue = []

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

        for i in queue:
            measure.remove(i)

        queue = []

    ### save the change to 'change-temp.xml' file
    tree.write('change-temp.xml')
    