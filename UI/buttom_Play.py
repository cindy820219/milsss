import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import tkinter.filedialog as filedialog

from xml.dom.minidom import parse
import xml.dom.minidom

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

### import other file
import for_parsing
import for_sheet
import for_modify

import sys, pygame, pygame.midi, time
from pygame.locals import *

### maybe it will be use! 
import subprocess
from threading import Thread

### for pygame and play wav
import pygame
import time

### import thread
import _thread
# import time

global note_x
note_x = []
note_x_1 = []
sort_note_x = []

MIDI_str = []
key_str = []

note = 0

note_queue = []

global w

global max_measure
max_measure = 0








# def run(max_measure):
#     measure = 1

#     canvas = Canvas(width = 980, height = 30, bg = 'yellow')
#     canvas.place(x= 265 ,y= -10)

#     arrow = PhotoImage(file = 'arrow.gif')
    
#     a = 5

#     ### 1
#     if (measure <= max_measure):
#         # canvas.create_image(20, 20, image = arrow, tag = "pic")
#         # canvas.update()
#         # time.sleep(1)
#         for i in range(20, 259, 10):
#             canvas.create_image(i, 20, image = arrow, tag = "pic")
#             canvas.update()
#             time.sleep(0.1)
#             canvas.delete('pic')
#         measure += 1

#     ### 2
#     if (measure <= max_measure):
#         # canvas.create_image(260, 20, image = arrow, tag = "pic")
#         # canvas.update()
#         # time.sleep(1)
#         canvas.delete('pic')
#         for i in range(260, 499, 10):
#             canvas.create_image(i, 20, image = arrow, tag = "pic")
#             canvas.update()
#             time.sleep(0.1)
#             canvas.delete('pic')
#         measure += 1

#     ### 3
#     if (measure <= max_measure):
#         # canvas.create_image(500, 20, image = arrow, tag = "pic")
#         # canvas.update()
#         # time.sleep(1)
#         for i in range(500, 739, 10):
#             canvas.create_image(i, 20, image = arrow, tag = "pic")
#             canvas.update()
#             time.sleep(0.1)
#             canvas.delete('pic')
#         measure += 1

#     ### 4 
#     if (measure <= max_measure):
#         # canvas.create_image(740, 20, image = arrow, tag = "pic")
#         # canvas.update()
#         # time.sleep(1)
#         for i in range(740, 1000, 10):
#             canvas.create_image(i, 20, image = arrow, tag = "pic")
#             canvas.update()
#             time.sleep(0.1)
#             canvas.delete('pic')
#         measure += 1

    ### 5
    # canvas = Canvas(width = 980, height = 30, bg = 'yellow')
    # canvas.place(x= 265 ,y= -10)

    # if (measure <= max_measure):
    #     # canvas.create_image(740, 20, image = arrow, tag = "pic")
    #     # canvas.update()
    #     # time.sleep(1)
    #     for i in range(20, 259, 10):
    #         canvas.create_image(i, 20, image = arrow, tag = "pic")
    #         canvas.update()
    #         time.sleep(0.1)
    #         canvas.delete('pic')
    #     measure += 1






### class!!! 
class worker(Thread):
    def run(self):
        pygame.init()

        pygame.midi.init()
        inp = pygame.midi.Input(1)
             
        # run the event loop
        while True:
            if (inp.poll()):
                note = inp.read(10)
                print (note)

class waiter(Thread):
    def run(self):
        for x in range(100,103):
            print (x)
            time.sleep(5)

def readMIDI():

    start = time.time()
    # print("hello")
    end = time.time()
    print(end - start)
    # print("hello")

    pygame.init()

    pygame.midi.init()
    inp = pygame.midi.Input(1)

    ### clear all the notes
    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x= 536+134, y=705)
    label_notes.image = empty # keep a ref


    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x=556+134, y=705)
    label_notes.image = empty # keep a ref
    
    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x=575+134, y=705)
    label_notes.image = empty # keep a re

    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x=593+134, y=705)
    label_notes.image = empty # keep a re

    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x=612+134, y=705)
    label_notes.image = empty # keep a re

    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x=631+134, y=705)
    label_notes.image = empty # keep a re

    empty = PhotoImage(file = 'empty.gif')
    label_notes = Label(image = empty)
    label_notes.place(x=651+134, y=705)
    label_notes.image = empty # keep a re




    ### input the key board
    while True:
        if (inp.poll()):
            note = inp.read(10)
            print(note)

            MIDI_key = note[0][0][1]
            print (MIDI_key)
            print('------------------')

            ###### 做雙音彈奏判斷部分
                # .............
            ######
            right = PhotoImage(file = 'right.gif')
            label_notes = Label(image = right)

            # left = PhotoImage(file = 'left.gif')
            # label_notes = Label(image = left)


            if (MIDI_key == 60):
                print('60 C')
                # note_queue.append(60)
                # x=536
                # y=705
                label_notes.place(x= 536+134, y=705)
                label_notes.image = right # keep a reference!
                
                break

            elif (MIDI_key == 62):
                print('62 D')
                label_notes.place(x=556+134, y=705)
                label_notes.image = right # keep a reference!
                break

            elif (MIDI_key == 64):
                print('64 E')
                label_notes.place(x=575+134, y=705)
                label_notes.image = right # keep a reference!
                # note_queue.append(62)
                break

            elif (MIDI_key == 65):
                print('65 F')
                label_notes.place(x=593+134, y=705)
                label_notes.image = right # keep a reference!
                # note_queue.append(62)
                break

            elif (MIDI_key == 67):
                print('67 G')
                label_notes.place(x=612+134, y=705)
                label_notes.image = right # keep a reference!
                # note_queue.append(62)
                break

            elif (MIDI_key == 69):
                print('69 A')
                label_notes.place(x=631+134, y=705)
                label_notes.image = right # keep a reference!
                # note_queue.append(62)
                break

            elif (MIDI_key == 71):
                print('71 B')
                label_notes.place(x=651+134, y=705)
                label_notes.image = right # keep a reference!
                # note_queue.append(62)
                break


    # print(note_queue)
            # time.sleep(3)

            # left = PhotoImage(file = 'empty.gif')
            # label_notes = Label(image = left)
            # label_notes.place(x, y)
            # label_notes.image = left # keep a reference!
            # note_queue.append(62)

            
# if(note_queue[1] == 62):
    


def print_time( threadName, delay):
    # count = 0
    # while count < 5:
    #   time.sleep(delay)
    #   count += 1
    #   print( threadName)

    print('in the thread!!!!!')

    pygame.init()
    pygame.mixer.music.load("wav.wav")

    pygame.mixer.music.play()
    time.sleep(10)


def buttomPlay(w, filename ,Li, Pr, Pl, Tem, note_x, key_x_str, key_y_str, hands, MIDI_str):
    # print('buttom note: ',note_x )
    # print('len note: ',len(note_x)

    # left = PhotoImage(file = 'left.gif')
    # label_notes = Label(image = left)
    # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    # label_notes.place(x=670, y=705)
    # label_notes.image = left # keep a reference!

    # print('MIDI_str: ', MIDI_str)
 

    global note_x_1

    filename = 'change-temp.xml'

    note_x = []
    
    ### for parsing and got the beats
    # collection, note_x, MIDI_str, key_x_str, key_y_str, hands
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(w, collection, note_x, MIDI_str, key_x_str, key_y_str, hands)

    ### got the time
    times = collection.getElementsByTagName('time')
    for beats in times:
        beats = beats.getElementsByTagName('beats')[0]
        beats = beats.childNodes[0].data

    ### print('note_x = []', note_x )
    print('Li, Pr, Pl, Tem: ',Li, Pr, Pl, Tem)
    
    ### count the measure
    tree = parse('change-temp.xml')
    root = tree.getroot()

    ### count max_measure
    max_measure = 0

    for measure in root.iter('measure'):
        max_measure += 1
    # print('max_measire: ',max_measure)

    ### Listen mode
    ### Listen mode
    ### Listen mode
    if (Li == 1):
        print('Listen mode')

        try:
           _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
           # _thread.start_new_thread( print_time, ("Thread-2", 4, ) )

        except:
           print ("Error: cant start the thread!")



        ### picture
        # quarter = PhotoImage(file = '4d5 new.gif')
        # label_notes = Label(image = quarter)
        # #label.grid(row = 3, column = 1, padx = 5, pady = 5)
        # label_notes.place(x=200,y=100)
        # label_notes.image = quarter # keep a reference!


        ### play music
        # pygame.init()
        # pygame.mixer.music.load("wav.wav")

        # pygame.mixer.music.play()
        # time.sleep(10)



        





        ### function arrow
        # run(max_measure)

        ### class arrow
        # worker().start()
        # waiter().start()

        ### Wang's class
        # ThreadForTagMove.start()

        ### defined in class
        # class ThreadForTagMove(Thread):
        #     def __init__(self, thread_id, name, counter):
        #         threading.Thread.__init__(self)
        #         self.thread_id = thread_id
        #         self.name = name
        #         self.counter = counter
        #         self.tag = 0
        #         self.daemon = True
            
        
        #     canvas = Canvas(width = 980, height = 30) #, bg = 'yellow')
        #     canvas.place(x= 265 ,y= -10)

        #     arrow = PhotoImage(file = 'arrow.gif')
            
        #     measure = 1

        #     ### 1
        #     if (measure <= max_measure):
        #         # canvas.create_image(20, 20, image = arrow, tag = "pic")
        #         # canvas.update()
        #         # time.sleep(1)
        #         for i in range(20, 259, 10):
        #             canvas.create_image(i, 20, image = arrow, tag = "pic")
        #             canvas.update()
        #             time.sleep(0.1)
        #             canvas.delete('pic')
        #         measure += 1

        #     ### 2
        #     if (measure <= max_measure):
        #         # canvas.create_image(260, 20, image = arrow, tag = "pic")
        #         # canvas.update()
        #         # time.sleep(1)
        #         canvas.delete('pic')
        #         for i in range(260, 499, 10):
        #             canvas.create_image(i, 20, image = arrow, tag = "pic")
        #             canvas.update()
        #             time.sleep(0.1)
        #             canvas.delete('pic')
        #         measure += 1

        #     ### 3
        #     if (measure <= max_measure):
        #         # canvas.create_image(500, 20, image = arrow, tag = "pic")
        #         # canvas.update()
        #         # time.sleep(1)
        #         for i in range(500, 739, 10):
        #             canvas.create_image(i, 20, image = arrow, tag = "pic")
        #             canvas.update()
        #             time.sleep(0.1)
        #             canvas.delete('pic')
        #         measure += 1

        #     ### 4 
        #     if (measure <= max_measure):
        #         # canvas.create_image(740, 20, image = arrow, tag = "pic")
        #         # canvas.update()
        #         # time.sleep(1)
        #         for i in range(740, 1000, 10):
        #             canvas.create_image(i, 20, image = arrow, tag = "pic")
        #             canvas.update()
        #             time.sleep(0.1)
        #             canvas.delete('pic')
        #         measure += 1


            # for i in range(200, 300, 10):
            #     print(i)
            #     canvas.create_image(i, 20, image = arrow, tag = "pic")
            #     canvas.update()
            #     time.sleep(0.1)
            #     canvas.delete('pic')

    ### Listen mode
    ### Listen mode
    ### Listen mode



    ### Practice mode 
    if (Pr == 1):
        print('Practice mode')
        # print('note_x: ',note_x)
        # print(len(note_x))
        lenth = len(note_x)
        # print('note_x.sort: ', sorted(note_x))
        
        ### for 5-9 str of notes!!! 
        for i in range(len(note_x)-1):
            if((note_x[i]) - (note_x[i+1]) > 460 ):
                ## print('!!!!!! there must next string: ',note_x[i], note_x[i+1])
                ## note_x_1.append(note_x[i+1])
                ## print('note_x_1: ',note_x_1)
                ## print(note_x[i+1], note_x[lenth-1])
                ### print(note_x[(i+1):(lenth-1)])
                
                note_x_1 = note_x[ (i+1) : (lenth-1) ]
                note_x = note_x[0: i]

                ## print('note_x: ',note_x)
                ## print('note_x_1: ',note_x_1)

                break

        ### note_x -----------------------------------------------
        arrow = PhotoImage(file = 'arrow.gif')
        sort_note_x = sorted(note_x)
        len_note_x = len(note_x)
        ## print('sorted note_x: ', sort_note_x)
        ## print(sort_note_x.pop(0))

        ### default canvas: create the canvas, size in pixels
        canvas = Canvas(width = 920, height = 30) #, bg = 'yellow')
        canvas.place(x= 270 ,y=-10)


        for i in range (len_note_x):
            x = sort_note_x.pop(0) - 260 
            canvas.create_image(x, 20, image = arrow, tag = "pic")
            canvas.update()
            
            readMIDI()
            # readMIDI().start()

            canvas.delete('pic')
        ### -------------------------------------------------------


        ### note_x_1 ----------------------------------------------
        
        sort_note_x_1 = sorted(note_x_1)
        len_note_x_1 = len(note_x_1)
        ## print('sorted note_x: ', sort_note_x.pop(0))
        ## print(sort_note_x.pop(0))

        ### default canvas: create the canvas, size in pixels
        # canvas = Canvas(width = 920, height = 30) # bg = 'yellow')
        # canvas.place(x= 270 ,y= 160)

        # for i in range (len_note_x_1):
        #     x = sort_note_x_1.pop(0) - 260 
        #     canvas.create_image(x, 20, image = arrow, tag = "pic")
        #     canvas.update()
        #     time.sleep(0.2)
        #     canvas.delete('pic')

        ### -------------------------------------------------------

    ### Play mode
    if (Pl ==1):
        print('Play mode')
        # for_line.continue_line(Tem, filename, beats)