### import parsing
from xml.dom.minidom import parse
import xml.dom.minidom

### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse

def simple_dual(DOMTree, collection):
    ### ????
    a = 0

    ### count all the chord notes
    chord_num = 0

    ### to count the number of three dual notes
    chord_pre = 0
    chord_now = 0
    chord_three = 0
    
    ### to count the total PI
    total_PI = 1

    ### test !!! not on the on-beat dual notes
    count_rest = 0

    ### parsing the file
    tree = parse('sonatina2.xml')
    root = tree.getroot()

    ### pre notes
    daul_pre_note = ''
    daul_staff_data = ''

    ### default measure_max and measure_num
    measure_max = 0
    measure_num = 0

    for measure in root.iter('measure'):
        measure_max = measure_max +1

    
    ### write to the test_dual.xml
    low_dual_func(root, tree)
    # high_dual_fun(root, tree)

# def high_dual_fun():

def low_dual_func(root, tree):
    ### low !!!

    ### count all the chord notes
    chord_num = 0

    ### to count the number of three dual notes
    chord_pre = 0
    chord_now = 0
    chord_three = 0

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
     

            ### left hand delete 'chord'
            if(chord != None and daul_staff_data == '2'):
                xml.etree.ElementTree.SubElement(note, 'rest')

                xml.etree.ElementTree.SubElement(note, 'chord_delete')
                note.find('chord_delete').text = 'yes'

            ### right hand delete 'chord'
            if(chord != None and daul_staff_data == '1'):
                xml.etree.ElementTree.SubElement(daul_pre_note, 'chord_delete')
                daul_pre_note.find('chord_delete').text = 'yes'                            
                
                if(note.find('chord') != None):
                    chord =  note.find('chord')
                    note.remove(chord)
            

            daul_pre_note = note
            chord_pre = chord_now

    ### here is delete the notes !!!
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            if(note.find('chord_delete') != None):
                measure.remove(note)

    tree.write('delete_low_dual.xml')

DOMTree = xml.dom.minidom.parse('sonatina2.xml')
collection = DOMTree.documentElement

hands = 0
simple_dual(DOMTree, collection)

