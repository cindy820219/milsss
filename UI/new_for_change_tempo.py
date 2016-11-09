### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse

### def funtion write_xml
# def write_xml(tree, out_path):
#     tree.write(out_path, encoding="utf-8",xml_declaration=True)

def change_tempo(filename ,Tem):

    ### if daul or accent is changed, then read file named 'change-temp.xml'
    # if (accent == 1 or daul == 1 or Tona == 1):
    #     filename = 'change-temp.xml'

    # ### global DOMTree, collection, tree
    # global DOMTree, collection, tree

    ### read the filename
    tree = parse(filename)
    root = tree.getroot()

    # change the attr - tempo:
    for per_minute in tree.iter('per-minute'):
        per_minute.text = ''
        Tem = str(Tem)
        per_minute.text += Tem
        # print("tempo change 1: ", per_minute.text)

    for sound in tree.iter('sound'):
        #print(sound.attrib)
        sound.set("tempo", Tem)
        # print("tempo change: ", sound.attrib)
       
        tree.write('change-tempo.xml')
        tree.write('change-temp.xml')
        print('  the file "change-tempo.xml" is saved.')


Tem = '40'
filename = 'sonatina.xml'
change_tempo(filename, Tem)