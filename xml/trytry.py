import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree,Element
from xml.dom.minidom import parse


tree = ET.parse('two-hand-3.xml')
root = tree.getroot()


for notes in root.iter('note'):
    new_x = notes.attrib
    break

if(new_x == {"default-x":"96.29","default-y": "-35.00"}):
    print('aaaa')
    # print(notes.attrib)


if (root.find("part/measure")):
	user = root.find("part/measure")
	user.remove(user.find("note"))

print(root.toxml())

# print(dom.toxml())
# user.remove(user.find("name"))
   
# print('aaa',root[3][0][3][0].attrib)
