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


##############

def simple_daul(filename):
    print(filename)
    filea = open('two-hand-2.xml', 'r')
    chord_part = open('chord_part.xml','w')
    chord_up = open('chord_up.xml','w')
    
    fileaString = filea.read()

    ### find measure location and count the site
    idFilter = 'measure'
    idPosition = fileaString.find(idFilter)
    count = filea.seek(idPosition,0)

    # print(fileaString[0:count-1])
    chord_up.write(fileaString[0:count-1])

    # print(fileaString[count-1:-28])
    chord_part.write(fileaString[count-1:-28])
    # filea.write('hahahhahahahahahah') 
    # chord_part = open('chord-part.xml', 'w')

    filea.close()
    chord_up.close()
    chord_part.close()
    
    print('aaaaaaa')

    tree_a = read_xml('chord_part.xml')
    print('bbbbbbb')
    root = tree_a.getroot()

    

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
            print('cccccccs')

    tree.write('chord_sim.xml')    

    

    create_newxml = open('chord_up.xml', 'a+')
    chord_sim = open('chord_sim.xml', 'r')

    # print(chord_sim.read())
    create_newxml.write(chord_sim.read())
    create_newxml.write('</part> </score-partwise>')
    create_newxml.close()
    chord_sim.close()

    