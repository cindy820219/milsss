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

def change_Tona_change_notes(filename,add_key):

    tree = parse(filename)
    root = tree.getroot()
    ######
    # <step>F</step>
    # <alter>1</alter>
    # <octave>4</octave>
    ######
    for measure in root.iter('measure'):
        for note in measure.iter('note'):
            for pitch in note.iter('pitch'):
                alter_nun = 0
                for step in pitch.iter('step'):
                    # print('step: ',step.text)
                    step_text = step.text
                for octave in pitch.iter('octave'):
                    # print('octave: ',octave.text)
                    octave_text = octave.text
                
                if(pitch.iter('alter')):
                    for alter in pitch.iter('alter'):
                        alter = alter.text
                        alter_nun = int(alter)

                print(step_text,octave_text)

                octave_num = (int(octave_text)+1) * 12
                
                if(step_text == 'C'):
                    step_num = 0

                if(step_text == 'D'):
                    step_num = 2

                if(step_text == 'E'):
                    step_num = 4

                if(step_text == 'F'):
                    step_num = 5

                if(step_text == 'G'):
                    step_num = 7

                if(step_text == 'A'):
                    step_num = 9

                if(step_text == 'B'):
                    step_num = 11

                midi = step_num + octave_num + alter_nun
                # print('Midi: ', midi )
                new_midi = midi + add_key
                # print('New Midi: ', new_midi)

                new_octave = (new_midi // 12) -1
                new_step = new_midi % 12

                if(new_step == 0):
                    new_step = 'C'
                if(new_step == 1):
                    new_step = 'C'

                if(new_step == 2):
                    new_step = 'D'
                if(new_step == 3):
                    new_step = 'D'

                if(new_step == 4):
                    new_step = 'E'

                if(new_step == 5):
                    new_step = 'F'
                if(new_step == 6):
                    new_step = 'F'

                if(new_step == 7):
                    new_step = 'G'
                if(new_step == 8):
                    new_step = 'G'
                
                if(new_step == 9):
                    new_step = 'A'
                if(new_step == 10):
                    new_step = 'A'
                
                if(new_step == 11):
                    new_step = 'B'
    
                step.text = ''
                step.text += new_step

                octave.text = ''
                octave.text += str(new_octave)

                # print('new: ',step.text, octave.text)
                
                write_xml(tree, 'change-key-note.xml')
    print('  the file "change-key-note" is saved.')    


def change_Tona(filename,Tona):
    
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    tree = read_xml(filename)
    
    Tona_str = ''

    if(Tona == 'C'):
        Tona_str = '0'
        Tona_num = 60

    if(Tona == 'D'):
        Tona_str = '2'
        Tona_num = 62

    if(Tona == 'E'):
        Tona_str = '4'
        Tona_num = 64

    if(Tona == 'F'):
        Tona_str = '6'
        Tona_num = 65

    if(Tona == 'G'):
        Tona_str = '1'
        Tona_num = 67

    if(Tona == 'A'):
        Tona_str = '3'
        Tona_num = 69

    if(Tona == 'B'):
        Tona_str = '5'
        Tona_num = 71
    
    # 屬性修改 - Tonality:
    for fifths in tree.iter('fifths'):
        # print('fifths.text:' ,fifths.text)
        pre_key = fifths.text
        # change the key
        fifths.text = ''
        fifths.text += Tona_str
        # print("key change : ", fifths.text)
        write_xml(tree, 'change-key.xml')
        print('  the file "change-key.xml" is saved.')

    if(pre_key == '0'):
        add_key = Tona_num - 60

    if(pre_key == '1'):
        add_key = Tona_num - 67

    if(pre_key == '2'):
        add_key = Tona_num - 62

    if(pre_key == '3'):
        add_key = Tona_num - 69

    if(pre_key == '4'):
        add_key = Tona_num - 64

    if(pre_key == '5'):
        add_key = Tona_num - 71

    if(pre_key == '6'):
        add_key = Tona_num - 65

    #if(pre_key == '7'):
    #    add_key = Tona_num - 61

    print('add_key: ',add_key)
    change_Tona_change_notes(filename,add_key)

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