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

def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

def change_tempo(filename ,Tem):

    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    tree = read_xml(filename)

    ### about the tempo
    directions = collection.getElementsByTagName('direction')
    # direction(directions)
    for direction in directions:
        per_minute = collection.getElementsByTagName('per-minute')[0]
        per_minute = per_minute.childNodes[0].data

    sounds = collection.getElementsByTagName('sound')
    for sound in sounds:
        if (sound.hasAttribute('tempo')):
            sound = sound.getAttribute('tempo')
            print('tempo original: ',sound)


    # 屬性修改 - tempo:
    for per_minute in tree.iter('per-minute'):
        per_minute.text = ''
        per_minute.text += Tem
        print("tempo change 1: ", per_minute.text)

    for sound in tree.iter('sound'):
        #print(sound.attrib)
        sound.set("tempo", Tem)
        print("tempo change 2: ", sound.attrib)
        #print(sound.attrib)
        write_xml(tree, "simple.xml")
        print('  the file "simple.xml" is saved.')

