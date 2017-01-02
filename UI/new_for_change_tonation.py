from xml.dom.minidom import parse
import xml.dom.minidom

### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse

import new_for_parse

def func_new_MIDI(new_MIDI):
    new_alter = '0'
    new_octave = (new_MIDI // 12 - 1)
    new_step_midi = (new_MIDI % 12)

    if(new_step_midi == 1 or new_step_midi == 3 or new_step_midi == 6 or new_step_midi == 8 or new_step_midi == 10):
        new_alter = '1'

    dict = {0:'C', 1:'C', 2:'D' ,3:'D' ,4:'E' ,5:'F' ,6:'F' ,7:'G' ,8:'G' ,9:'A' ,10:'A' ,11:'B' }
    new_step = dict[new_step_midi]

    # print(new_step)

    return (new_step, str(new_octave), new_alter)


def change_Tonation(filename, fifths, Tona):
    # print(filename)
    hands = 0
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement                    
    new_for_parse.parsing(DOMTree, collection, hands)

    # print('Tona: ', Tona)


    # d2 = {}
    ### #1 G   #2 D    #3 A    #4 E  ### b1 F   b2 bB   b3 bE   b4 bA
    dict = {'C': 0, 'G': 7, 'D': 2, 'A': -3, 'E': 4, 'B': -1, 'Gb': 6, 'F': 5, 'Bb': -2, 'Eb': 3, 'Ab': -4, 'Db': 1, '0':0, '1':7, '2':2, '3':-3, '4':4, '-1':5, '-2':-2, '-3':3, '-4':-4}
    
    # print('dict!!!!!' ,dict[Tona])
    # print('o: ', dict[fifths])
    # print('n: ', dict[Tona])
    add_key = dict[Tona]- dict[fifths]
    print( 'add key: ' , add_key)

    ### defind the MIDI_text
    MIDI_text =''

    tree = parse(filename)
    root = tree.getroot()

    for fifth in tree.iter('fifths'):
        if(Tona =='C'):
            fif = '0'
        if(Tona =='G'):
            fif = '1'
        if(Tona =='D'):
            fif = '2'
        if(Tona =='A'):
            fif = '3'
        if(Tona =='E'):
            fif = '4'
        if(Tona =='B'):
            fif = '5'

        if(Tona =='F'):
            fif = '-1'
        if(Tona =='Bb'):
            fif = '-2'
        if(Tona =='Eb'):
            fif = '-3'
        if(Tona =='Ab'):
            fif = '-4'
        if(Tona =='Db'):
            fif = '-5'

        fifth.text = fif

    # print(root)
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for Midi in note.iter('MIDI'):
                MIDI_text = Midi.text
                # print(MIDI_text)

                new_MIDI = int(MIDI_text)+add_key
                Midi.text = str(new_MIDI)
                # print(Midi.text)
                
                new = func_new_MIDI(new_MIDI)
                # print(new[0], new[1], new[2])
            

                for pitch in note.iter('pitch'):
                    for step in pitch.iter('step'):
                        step.text = new[0]
                    
                    for octave in pitch.iter('octave'):
                        octave.text = new[1]

                    altert = pitch.find('alter')

                    # ### if find 'alter'
                    if(altert != None):
                        for alter in pitch.iter('alter'):
                            alter.text = new[2]
                    ### if not find 'alter', add node alter
                    else:
                        xml.etree.ElementTree.SubElement(pitch, 'alter')
                        pitch.find('alter').text = new[2]      
                        
    tree.write('change_tonation.xml')
    print(' ---------->  have change tonational')
    tree.write('change_temp.xml')
