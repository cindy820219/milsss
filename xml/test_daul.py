import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element
# tree = ET.parse('chord.xml')
# root = tree.getroot()
tree = parse('chord_part.xml')
root = tree.getroot()

# root.remove(root.find('note'))


for note in root.iter('note'):
    print('note')
    #duration = note.find('duration').text
    #print(duration)

    chord =  note.find('chord')
### 要刪除的音
    if(chord != None):
        print(chord)
        root.remove(note)
        print('delete')

tree.write('chord-sim.xml')