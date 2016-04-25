import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom
import math

from xml.etree.ElementTree import ElementTree, Element

import for_sheet
import for_parsing

# import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse

global fileaString


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
        write_xml(tree, 'change-key.xml')
        print('  the file "change-key.xml" is saved.')


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
        write_xml(tree, "change-tem.xml")
        print('  the file "change-tem.xml" is saved.')

def simple_daul(filename):
    chord_sim = open('change-daul.xml','w')

    tree = parse(filename)
    root = tree.getroot()

    queue = []

    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            ### 要刪除的音
            chord =  note.find('chord')
            
            if(chord != None):
                queue.append(note)
        # print('queue: ',queue)
        
        for i in queue:
            measure.remove(i)
            # measure.remove(queue.pop(0))
            # print('deleted queue[0]: ',queue)

        queue = []

    tree.write('change-daul.xml')
    print('  the file "change-daul.xml" is saved.')