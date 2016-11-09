from xml.etree.ElementTree import ElementTree, Element, parse
import xml.etree.ElementTree 

def change_hand(filename, hand):
    print(filename)
    print('hand: ', hand)
    
    tree = parse(filename)
    root = tree.getroot()

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for staff in note.iter('staff'):
                staff_text = staff.text
                print(staff_text)
                if(staff_text != hand):
                    if(note.find('rest') != None):
                        print('a' ,staff_text)
                        # xml.etree.ElementTree.SubElement(note, 'rest')
                    else:
                        print('b')
                        xml.etree.ElementTree.SubElement(note, 'rest')

    tree.write('change_hand.xml')
    print('  save the file name "change_hand.xml"')
