from xml.etree.ElementTree import ElementTree,Element

# read xml file
def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

# write xml file
def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

# match: node and kv_map: 属性及属性值组成的map
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

#---------- search ----------

def find_nodes(tree, path):
    '''
    查某個路徑匹配的所有節點
    tree: xml 樹
    path: 節點路徑
    '''
    return tree.findall(path)

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

#---------- change ----------

def change_node_properties(nodelist, kv_map, is_delete=False):
    '''
    修改/增加 /删除 節點的屬性及屬性值(attrib)
    nodelist: 節點列表
    kv_map: 属性及属性值map
    '''
    for node in nodelist:
        for key in kv_map:
            if is_delete: 
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))
            
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''
    改變/增加/删除一個節點的 text
    nodelist: 節點列表
    text : test
    '''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
            
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
        
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    '''
    通過屬性及屬性值定位一個節點，並刪除之
    nodelist: 父節點列表
    tag: 子節點標籤
    kv_map: 屬性及屬性值列表
    '''
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)


if __name__ == "__main__":

    tree = read_xml("modify-in.xml")
    
    # A. 屬性修改
    # 1. 找到父節點 (上一層 / 本層)
    nodes = find_nodes(tree, "processers/processer")
    # 2. 確認子節點
    result_nodes = get_node_by_keyvalue(nodes, {"name":"BProcesser"})
    # 3. 修改節點屬性值，增加 age = 1
    change_node_properties(result_nodes, {"age": "1"})
    # 4. 刪除節點屬性值
    # change_node_properties(result_nodes, {"value":""}, True)


    # B. 節點修改
    # 1. 新建節點 ("new node name", {attrbute 1,attrbute 2 }, content)
    a = create_node("person", {"age":"15","money":"200000"}, "the firest content")
    Ling = create_node("Ling", {},"this is Ling first change the xml file")
    # 2. 插入到父節點之下 (result_nodes 底下)
    # add_child_node(result_nodes, a)
    add_child_node(result_nodes, Ling)

    
    # C. 刪除節點
    # 1. 定位父節點
    del_parent_nodes = find_nodes(tree, "processers/services/aaa")
    # 2. 準確定位子節點並刪除之
    target_del_node = del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency" : "chain1"})
   
    # D. 修改節點本文
    # 定位節點
    text_nodes = get_node_by_keyvalue(find_nodes(tree, "processers/services/aaa/chain"), {"sequency":"chain3"})
    change_node_text(text_nodes, "new text")


    # 输出到结果文件
    write_xml(tree, "modify-out.xml")