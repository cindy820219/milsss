import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom
import math

from xml.etree.ElementTree import ElementTree,Element

import for_sheet
import for_parsing

def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

def change_Tona(filename,Tona):
    
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    tree = read_xml(filename)
    
    Tona_num = ''

    if(Tona == 'C'):
        Tona_num = '0'

    if(Tona == 'D'):
        Tona_num = '2'

    if(Tona == 'E'):
        Tona_num = '4'
    
    if(Tona == 'F'):
        Tona_num = '6'
    
    if(Tona == 'G'):
        Tona_num = '1'
    
    if(Tona == 'A'):
        Tona_num = '3'

    if(Tona == 'B'):
        Tona_num = '5'
    
    # 屬性修改 - Tonality:
    for fifths in tree.iter('fifths'):
        fifths.text = ''
        fifths.text += Tona_num
        # print("key change : ", fifths.text)
        write_xml(tree, 'key-change.xml')
        print('  the file "key-change.xml" is saved.')

    filename = 'key-change.xml'
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection)



def change_tempo(filename ,Tem):

    global DOMTree, collection, tree

    #DOMTree = xml.dom.minidom.parse(filename)
    #collection = DOMTree.documentElement
    tree = read_xml(filename)

    # 屬性修改 - tempo:
    for per_minute in tree.iter('per-minute'):
        per_minute.text = ''
        per_minute.text += Tem
        # print("tempo change 1: ", per_minute.text)

    for sound in tree.iter('sound'):
        #print(sound.attrib)
        sound.set("tempo", Tem)
        # print("tempo change: ", sound.attrib)
        #print(sound.attrib)
        write_xml(tree, "tem-change.xml")
        print('  the file "tem-change.xml" is saved.')

