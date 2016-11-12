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

                ### define and count the octave_num
                octave_num = (int(octave_text)+1) * 12
                # print(' !! octave_num: ',octave_num)
                
                ### oringe step
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

                ### count the midi 
                midi = step_num + octave_num + alter_nun
                # print('Midi: ', midi )

                ### count the new midi
                new_midi = midi + add_key
                # print('New Midi: ', new_midi)

                new_octave = (new_midi // 12) -1
                new_step = new_midi % 12

                ### C
                if(new_step == 0):
                    new_step = 'C'
                    ### delete all sharp
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)
                
                if(new_step == 1):
                    new_step = 'C'
                    ### add sharp
                    xml.etree.ElementTree.SubElement(note, 'accidental')
                    note.find('accidental').text = 'sharp'

                ### D
                if(new_step == 2):
                    new_step = 'D'
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)
                
                if(new_step == 3):
                    new_step = 'D'
                    xml.etree.ElementTree.SubElement(note, 'accidental')
                    note.find('accidental').text = 'sharp'

                ### E
                if(new_step == 4):
                    new_step = 'E'
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)

                ### F
                if(new_step == 5):
                    new_step = 'F'
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)
                
                if(new_step == 6):
                    new_step = 'F'
                    xml.etree.ElementTree.SubElement(note, 'accidental')
                    note.find('accidental').text = 'sharp'

                ### G
                if(new_step == 7):
                    new_step = 'G'
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)
                
                if(new_step == 8):
                    new_step = 'G'
                    xml.etree.ElementTree.SubElement(note, 'accidental')
                    note.find('accidental').text = 'sharp'
            
                ### A
                if(new_step == 9):
                    new_step = 'A'
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)
                
                if(new_step == 10):
                    new_step = 'A'
                    xml.etree.ElementTree.SubElement(note, 'accidental')
                    note.find('accidental').text = 'sharp'

                ### B
                if(new_step == 11):
                    # if(note.find('accidental') != None):
                        # print('gooooood')

                    new_step = 'B'
                    if(note.find('accidental') != None):
                        acci =  note.find('accidental')
                        note.remove(acci)
                    if(pitch.find('alter') != None):
                        alt = pitch.find('alter')
                        pitch.remove(alt)
    
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
    
    ### parsing the file
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    tree = read_xml(filename)
    
    ### change tonation str
    Tona_str = ''
    pre_fifths = ''

    # print('Tona: ',Tona)
    
    ### default add_key
    add_key = 0

    ### define the change tonation num and str
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
        print('  is me !! pre_key: ', pre_key)
        
        if(pre_key == '-1' or pre_key == '6'):
            pre_fifths = '6'

        ### to bool if must to change tonality
        if (pre_fifths != Tona_str):
            # change the key
            fifths.text = ''
            fifths.text += Tona_str
            print('key change : ', fifths.text)
        
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

    if(pre_key == '-1'):
        add_key = Tona_num - 65

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
    # add_key = 5
    change_Tona_change_notes(filename, add_key)