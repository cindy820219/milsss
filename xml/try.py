import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree,Element
from xml.dom.minidom import parse
'''
tree = ET.parse('two-hand-2.xml')
root = tree.getroot()


for notes in root.iter('note'):
    print(notes.attrib)
    print(root[3][0][3][1].text)
'''

def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def create_node(tag, property_map, content):
    '''
    create a new note
    tag: 節點的tag
    property_map: 屬性及屬性值map
    content: 節點閉合標籤裡的文本內容
    return new note
    '''
    element = Element(tag, property_map)
    element.text = content
    return element

def add_child_node(nodelist, element):
    '''
    給一個節點添加子節點
    nodelist: 節點列表
    element: 子節點
    '''
    for node in nodelist:
        node.append(element)

def get_node_by_keyvalue(nodelist, kv_map):
    '''
    根據屬性及屬性質定位符合的節點返回節點
    nodelist: 節點列表
    kv_map: 匹配屬性及屬性質 map
    '''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
            # print(result_nodes)
    return result_nodes

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

def if_match(node, kv_map):
    '''
    判斷某個節點是否包含所有傳入參數屬性
    node: 節點
    kv_map: 屬性及屬性質所形成的 map 
    '''
    for key in kv_map:
        if(node.get(key) != kv_map.get(key)):
            return False
    return True

if __name__ == "__main__":

    
    #tree = ElementTree()
    tree = read_xml("two-hand-3.xml")
    root = tree.getroot()
    notes = root[3]
    print(notes.tag)
    result_nodes = notes

    # B. 節點修改
    # 1. 新建節點 ("new node name", {attrbute 1,attrbute 2 }, content)
    a = create_node("direction", {"placement":"above"}, "")
    # Ling = create_node("Ling", {},"this is Ling first change the xml file")
    # 2. 插入到父節點之下 (result_nodes 底下)
    add_child_node(result_nodes, a)
    # add_child_node(result_nodes, Ling)



    dom = parse("two-hand-3.xml")
    x = dom.createElement("foo")
    txt = dom.createTextNode("hello, world!")
    x.appendChild(txt)
    dom.childNodes[1].appendChild(x)
    print(dom.toxml())

    # 输出到结果文件
    write_xml(tree, "modify-out.xml")