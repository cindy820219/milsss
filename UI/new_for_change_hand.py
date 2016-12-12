from xml.etree.ElementTree import ElementTree, Element, parse
import xml.etree.ElementTree 

def change_hand(filename, hand):
    hand_delete_queue=[]
    print(filename)
    print('hand: ', hand)
    
    tree = parse(filename)
    root = tree.getroot()

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for staff in note.iter('staff'):
                staff_text = staff.text
                # print(staff_text)
                # if(staff_text != hand):
                #     if(note.find('rest') != None):
                #         print('a')
                #         # xml.etree.ElementTree.SubElement(note, 'rest')
                #     else:
                #         # print('b')
                #         xml.etree.ElementTree.SubElement(note, 'rest')
                if(staff_text != hand):
                    hand_delete_queue.append(note)
                    print('hand_delete_queue: ', hand_delete_queue)
                    # measure.remove(note)

        
        for i in hand_delete_queue:
                measure.remove(i)
        hand_delete_queue = []

    # tree.write('change_hand.xml')
    tree.write('change_temp.xml')
    # print('  save the file name "change_hand.xml"')
    print(' ---------->  have change hands')
