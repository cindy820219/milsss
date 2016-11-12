

def change_Tonation(filename, Tona):

    ### parsing the file
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    