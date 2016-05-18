
'''
from xml.etree.ElementTree import ElementTree, Element,  SubElement

# import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse

from copy import deepcopy
import xml.etree.cElementTree as etree

#if __name__ == '__main__':
aaa = open('aaa.xml','w')

tree = parse('two-hand-1.xml')
root = tree.getroot()


root.append(Element('one'))
root.append(Element('two'))

# one = 'alter>1</alter'

# SubElement(root, 'alter>1</alter')

# root.append(etree.Comment("some comment"))

#### root.append( etree.Element("child1") )
# child2 = etree.SubElement(root, "child2")
# child3 = etree.SubElement(root, "child3")

#### root.insert(0, etree.Element("child0"))


html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

etree.tostring(html)
### b'<html><body>TEXT</body></html>'

br = etree.SubElement(body, "br")
etree.tostring(html)
### b'<html><body>TEXT<br/></body></html>'

br.tail = "TAIL"
etree.tostring(html)
### b'<html><body>TEXT<br/>TAIL</body></html>'


alter = etree.Element("alter")
alter.text = "1"

print(etree.tostring(alter))

tree.write('aaa.xml')
print('  the file "aaa.xml" is saved.') 
'''   
a = 11
b =	3
c = 23



y = []
y.append(a)
y.append(b)
y.append(c)


print('y: ',y)
s = y
print('s: ',s)
yy = y.sort()
print('y sort: ',yy)