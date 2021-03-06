### import tk
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

from tkinter import messagebox

### import keyboard and thread
from threading import Thread
import _thread
import sys, pygame, pygame.midi, time
from pygame.locals import *

import pygame
import time

### import minidom
from xml.dom.minidom import parse
import xml.dom.minidom

### import ElementTree
from xml.etree.ElementTree import ElementTree, Element, parse


'''
import all the function 

for_parsing - parse
for_sheet- draw the sheet
buttom_Play - when the Play button is click
'''
import new_for_change_tempo
import new_for_sim_rhythm
import new_for_change_hand
import new_for_sim_dual
import new_for_parse
import new_for_change_tonation

# from for_sheet import key_location, create_notes

# import buttom_Play


### call the external command
from subprocess import call
import os



# from PIL import *
# from PIL import Image, ImageTk

def default(collection):
    attrs = collection.getElementsByTagName('attributes')
    for attr in attrs:
        keys = collection.getElementsByTagName('key')
        for key in keys:
            global fifths
            fifths = key.getElementsByTagName('fifths')[0]
            fifths = fifths.childNodes[0].data

            # global fifths
            # print('key:' ,fifths)

        times = collection.getElementsByTagName('time')
        for time in times:
            beats = time.getElementsByTagName('beats')[0]
            beattype = time.getElementsByTagName('beat-type')[0]

            beats = beats.childNodes[0].data
            beattype = beattype.childNodes[0].data

            # print('times: ',beats+'/'+beattype+' ')
            
    ### about the write tempo
    directions = collection.getElementsByTagName('direction')
    for direction in directions:
        per_minute = collection.getElementsByTagName('per-minute')[0]
        per_minute = per_minute.childNodes[0].data

    ### about the real tempo
    sounds = collection.getElementsByTagName('sound')
    for sound in sounds:
        if (sound.hasAttribute('tempo')):
            sound = sound.getAttribute('tempo')
            # print('tempo: ',sound)

    global Default_Tona 

    ### Default_Tona
    if (fifths == '0'):
        Default_Tona = 'C'
    if (fifths == '1'):
        Default_Tona = 'G'
    if (fifths == '2'):
        Default_Tona = 'D'
    if (fifths == '3'):
        Default_Tona = 'A'
    if (fifths == '4'):
        Default_Tona = 'E'
    if (fifths == '5'):
        Default_Tona = 'B'
        # print('  is too difficult!')
        # messagebox.showinfo("Alter", "Toooo difficult")
    if (fifths == '6'):
        Default_Tona = 'Gb'
        # print('  is too difficult!')
        # messagebox.showinfo("Alter ", "Toooo difficult")
    if (fifths == '7'):
        Default_Tona = 'C'
        print('  is too difficult!')
        messagebox.showinfo("Alter ", "Toooo difficult")


    if (fifths == '-1'):
        Default_Tona = 'F'
    if (fifths == '-2'):
        Default_Tona = 'Bb'
    if (fifths == '-3'):
        Default_Tona = 'Eb'
    if (fifths == '-4'):
        Default_Tona = 'Ab'
    if (fifths == '-5'):
        Default_Tona = 'Db'
        # messagebox.showinfo("Alter", "Toooo difficult")
    if (fifths == '-6'):
        Default_Tona = 'Gb'
        # messagebox.showinfo("Alter", "Toooo difficult")
    if (fifths == '-7'):
        Default_Tona = 'C'
        # print('  is too difficult!')
        # messagebox.showinfo("Alter ", "Toooo difficult")

    # print('Default_Tona: ',Default_Tona)
    return(Default_Tona, per_minute)

def openSample1():

    # global image
    # image.destroy()


    # label_image.config(image='')
    
    print('  open file : sonatina.xml')
    ### open XML with the MuseScore and save the file named : test-file.png
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/Samplesonatina.xml -o /Users/nien/Desktop/milsss/UI/file.png'
    os.system(cmd)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ### small 50% : test-file-1.png to small.png
    # cmd = 'convert file-1.png -resize 40% file_small.png'
    cmd = 'convert -quality 100 -resize 70% file-1.png file_small.gif'
    os.system(cmd)
    cmd = 'convert -quality 100 -resize 91% file_small.gif file_small.gif'
    os.system(cmd)

    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'file_small.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-250)
    label_image.image = image # keep a reference!


    ### turn the xml to wav
    # cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/Samplesonatina.xml -o /Users/nien/Desktop/milsss/UI/new_wav.wav'
    # os.system(cmd)

    ### filename
    global filename
    filename = '/Users/nien/Desktop/milsss/UI/Samplesonatina.xml'

    ### hand
    global hands
    hands = 0

    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement

    ### find the default
    default_tempo_tonation = default(collection)
    comboboxTona.set(default_tempo_tonation[0])
    scale.set(default_tempo_tonation[1])

def openSample2():
    print('open file : sonatina2.xml')
    ### open XML with the MuseScore and save the file named : test-file.png
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/Samplesonatina2.xml -o /Users/nien/Desktop/milsss/UI/file.png'
    os.system(cmd)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ### small 50% : test-file-1.png to small.png
    # cmd = 'convert file-1.png -resize 40% file_small.png'
    cmd = 'convert -quality 100 -resize 70% file-1.png file_small.gif'
    os.system(cmd)
    cmd = 'convert -quality 100 -resize 91% file_small.gif file_small.gif'
    os.system(cmd)
    # cmd = 'convert -quality 100 -resize 95% file_small.gif file_small.gif'
    # os.system(cmd)  

    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'file_small.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-250)
    label_image.image = image # keep a reference!

    ### turn the xml to wav
    # cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/Samplesonatina2.xml -o /Users/nien/Desktop/milsss/UI/new_wav.wav'
    # os.system(cmd)

    ### filename
    global filename
    filename = '/Users/nien/Desktop/milsss/UI/Samplesonatina2.xml'

    ### hand
    # global hands
    # hands = 0

    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement

    ### find the default
    default_tempo_tonation = default(collection)
    comboboxTona.set(default_tempo_tonation[0])
    scale.set(default_tempo_tonation[1])

def openfile():
    ### choose the file named '*.mid' & '*.xml'
    global filename
    filename = root.fileName = filedialog.askopenfilename( filetypes = (("Musicxml","*.xml"),("midi file","*.mid")))
    print(root.fileName)
    print(' --------------------filename:', filename)
    
    tree = parse(filename)
    aroot = tree.getroot()

    ### change the page-width
    for page in aroot.iter('page-width'):
        # print(page.text)
        page.text = '980'
    tree.write(filename)

    cmd = 'sudo '
    cmd1 = '/Applications/MuseScore\ 2.app/Contents/MacOS/mscore '
    cmd2 = filename
    cmd3 = ' -o /Users/nien/Desktop/milsss/UI/file.png'
    # print('aaaaa: ',cmd + cmd1  + cmd2 + cmd3)
    os.system(cmd + cmd1  + cmd2 + cmd3)

    # cmd = 'convert file-1.png -resize 40% file_small.png'
    cmd = 'convert -quality 100 -resize 70% file-1.png file_small.gif'
    os.system(cmd)
    cmd = 'convert -quality 100 -resize 91% file_small.gif file_small.gif'
    os.system(cmd)


    ### turn the xml to wav
    # cmd = 'sudo '
    # cmd1 = '/Applications/MuseScore\ 2.app/Contents/MacOS/mscore '
    # cmd2 = filename
    # cmd3 = ' -o /Users/nien/Desktop/milsss/UI/new_wav.wav'
    # # print('aaaaa: ',cmd + cmd1  + cmd2 + cmd3)
    # os.system(cmd + cmd1  + cmd2 + cmd3)


    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'file_small.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-250)
    label_image.image = image # keep a reference!

    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement

    ### find the default
    default_tempo_tonation = default(collection)
    comboboxTona.set(default_tempo_tonation[0])
    scale.set(default_tempo_tonation[1])

### def function OK button
def buttonOKClicked():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('It is click OK !!!')

    global filename
    refilename = filename
    # print(refilename)
    
    ### default the Mode, Tonation and Tempo
    Mode = Tona = Tem = ''
    
    # hands = 0
    # DOMTree = xml.dom.minidom.parse(filename)
    # collection = DOMTree.documentElement

    # new_for_parse.parsing(DOMTree, collection, hands)

    '''
    if both  hand, hands = 0
    if right hand, hands = 1
    if left  hand, hands = 2
    '''
    hands = 0
    hand_is_change = 0
    tempo_is_change = 0
    rhythm_is_change = 0
    dual_is_change = 0

    ### Tem
    Tem = var.get()
    print('Tempo: ',Tem)

    ### hand
    hand = str(radio_hand.get())
    print('hand: ', hand)

    # print("Dual: ",var1.get(), ",  Rhythm: ",var3.get()) ###, "Rhythm: ",var2.get(), "Accent: ",var3.get())
    # dual = var1.get()
    # rhythm = var3.get()

    ### radio for level : hight level = 2, low level = 1, level = 0
    level = int(radio_level.get())
    # print('level Dual: ', level)

    # ### dual special !!!!!!!!! ### 
    # # if(level != 0):
    # if(level == 2):
    #     print(' ---------->  go to the dual  high simple 2')
    #     DOMTree = xml.dom.minidom.parse(filename)
    #     collection = DOMTree.documentElement
    #     hands = 0
                    
    #     new_for_parse.parsing(DOMTree, collection, hands)
    #     filename = 'change_parse.xml'
    #     # change_parse.xml

    #     DOMTree = xml.dom.minidom.parse(filename)
    #     collection = DOMTree.documentElement

    #     new_for_sim_dual.simple_dual(DOMTree, collection, level)

        
    #     # filename = refilename






    #     print('  ~~~~~~~  refilename', refilename)
    #     filenametwo = refilename.replace('UI', 'Sample')

    #     # print('  ~~~~~~~  newwwwwwwwww:', filenameone)
    #     print('  ~~~~~~~  newwwwwwwwww:', filenametwo)

    #     # filenameone = '/Users/nien/Desktop/milsss/Sample/'+filename
    #     # filename = filenameone
    #     # print('filenameone:', filenameone)
    #     filename = filenametwo
    
    # print('1: ',filename)
    
    # if( filename == True):
    #     print('File is in the Sample')
    #     print('2: ',filename)
    # else:
    #     filename = filename.replace('Sample', 'UI')
    #     # print('hahahahahhahahahahahahahah  5  ',filename)
    #     print('3: ',filename)

    # print('4: ',filename)




    level_radio_rhythm = int(radio_rhythm.get())
    # print('level rhythm: ', level_radio_rhythm)

    # get Tonality value
    Tona = comboboxTona.get()
    print('Tona: ',Tona)

    ### ### ### ###    

    print(' ---------->  is tempo change')
    new_for_change_tempo.change_tempo(filename ,Tem)
    print('           hereherehere filename:', filename)
    filename = 'change_temp.xml'
    ### ### ### ###

    ''' 
    check the file name and get Mode, Tonation and Tempo
    get Rhythm from var3
    get daul   from var1
    '''

    ### ### ### ###
    if(hand != '0'): 
        print(' ---------->  is hand change')
        # hand_is_change = 1
        new_for_change_hand.change_hand(filename, hand)

    ### ### ### ###
    

    
    ### ### ### ###
    ### daul low !!!!!!!
    if(level == 1):
        print('in low level dual function')
        print(' ---------->  go to the dual low simple 1')
        tree = parse(filename)
        root = tree.getroot()
        
        new_for_sim_dual.low_dual_func(root, tree)
        # print('out')

        # if(level == 2):
        #     print(' ---------->  go to the dual  high simple 2')
        #     DOMTree = xml.dom.minidom.parse(filename)
        #     collection = DOMTree.documentElement
        #     hands = 0
                        
        #     new_for_parse.parsing(DOMTree, collection, hands)
        #     filename = 'change_parse.xml'
        #     # change_parse.xml

        #     DOMTree = xml.dom.minidom.parse(filename)
        #     collection = DOMTree.documentElement

        #     new_for_sim_dual.simple_dual(DOMTree, collection, level)

        #     filename = 'change_temp.xml'
    


    ### dual special !!!!!!!!! ### 
    # if(level != 0):
    if(level == 2):
        print(' ---------->  go to the dual  high simple 2')
        DOMTree = xml.dom.minidom.parse(filename)
        collection = DOMTree.documentElement
        hands = 0
                    
        new_for_parse.parsing(DOMTree, collection, hands)
        filename = 'change_parse.xml'
        # change_parse.xml

        DOMTree = xml.dom.minidom.parse(filename)
        collection = DOMTree.documentElement

        new_for_sim_dual.simple_dual(DOMTree, collection, level)
        
        filename = 'change_temp.xml'
        
    
    ### Rhythm !!!!!
    if(level_radio_rhythm != 0):
        print(' ---------->  go to rhythm simple')
        rhythm = 1
        DOMTree = xml.dom.minidom.parse(filename)
        collection = DOMTree.documentElement

        hands = 0
        new_for_sim_rhythm.rhythm_parsing(DOMTree, collection, hands, rhythm, level_radio_rhythm)
    ### ### ### ###
    
    # print('default original tonational: ', fifths)
    # print('change tona: ',Tona)
    # new_for_change_tonation.change_Tonation(filename, Tona)

    ### Tona new get, fifths origin
    # print('Default_Tona: ',Default_Tona)
    # print('Tona: ',Tona)
    if (Default_Tona != Tona):
        new_for_change_tonation.change_Tonation(filename, fifths, Tona)

    # cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/change_temp.xml -o /Users/nien/Desktop/milsss/UI/file.png'
    # os.system(cmd)

    # ### small 70%
    # cmd = 'convert -quality 100 -resize 70% file-1.png file_small.gif'
    # os.system(cmd)
    # cmd = 'convert -quality 100 -resize 91% file_small.gif file_small.gif'
    # os.system(cmd)
    # ### turn the xml to wav

    # cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/change_temp.xml -o /Users/nien/Desktop/milsss/UI/new_wav.wav'
    # os.system(cmd)

    # image = PhotoImage(file = 'test.gif-file.gif')
    # image = PhotoImage(file = 'file_small.gif')
    # label_image = Label(image = image)
    # label_image.place(x=180,y=-250)
    # label_image.image = image # keep a reference!

    # messagebox.showinfo("Yo", "It's finished !")

    ### open the muse
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/change_temp.xml'
    os.system(cmd)
    
# def play(x, y):    
#     pygame.mixer.music.load('new_wav.wav')
#     pygame.mixer.music.play()
#     ### add count lenth wav
#     time.sleep(10000)

#     # messagebox.showinfo("Over", "Play over")

# def buttonStopClicked():
#     pygame.mixer.music.stop()    

# def buttonPlayClicked():

#     Mode = comboboxMode.get()
#     print('Mode: ',Mode)    

#     ### init pygame and call the thread!
#     pygame.init()
#     th = Thread(target=play, args=(1,2))
#     th.start()

# def onKeyPress(event):
#     print('You pressed %s\n' % (event.char, ))

def main():
    ### global all the event
    global label_2, label_3, label_4, label_keyboard
    global comboboxMode, comboboxTona, scale, var1, var2, var3, var, radio_hand, radio_level, radio_rhythm

    ### labal
    veiw = Frame(root,width="1450", height="700") 
    # veiw.grid(row=0,column=0)
    veiw.pack()

    ### radio for right or left hand
    radio_hand = IntVar()
    labal_7 = tk.Label(root,text='Hand').place(x=10, y=60) 
    Radiobutton(root, text='Both Hands', variable=radio_hand, value='0').place(x=60, y=40)
    Radiobutton(root, text='Only Right Hand', variable=radio_hand, value='1').place(x=60, y=60)
    Radiobutton(root, text='Only Left Hand', variable=radio_hand, value='2').place(x=60, y=80)



    # Checkbutton - Daul (var1), Rhythm (var2), Accent (var3)
    # var1 = IntVar()
    # Checkbutton(root, text="Dual", variable=var1).place(x=25,y=150)
    
    # var2 = IntVar()
    # # Checkbutton(root, text="Rhythm", variable=var2).place(x=70,y=50)
    
    # var3 = IntVar()
    # Checkbutton(root, text="Rhythm", variable=var3).place(x=25,y=220)

    
    label_5 = tk.Label(root,text='Dual').place(x=10, y=150) 
    label_6 = tk.Label(root,text='Rhythm').place(x=10, y=220) 

    ### radio for level_Dual
    radio_level = IntVar()
    # Radiobutton(root, text='Original', variable=radio_level, value='0').place(x=30, y=180)
    Radiobutton(root, text='Original (✭✭✭✭✭)', variable=radio_level, value='0').place(x=60, y=130)
    Radiobutton(root, text='High     (✭✭✭)', variable=radio_level, value='2').place(x=60, y=150)
    Radiobutton(root, text='Low      (✭)', variable=radio_level, value='1').place(x=60, y=170)

    ### radio for level_Rhythm
    radio_rhythm = IntVar()
    ###  state=DISABLED


    # Radiobutton(root, text='Original', variable=radio_level, value='0').place(x=30, y=180)
    Radiobutton(root, text='Original (✭✭✭✭✭)', variable=radio_rhythm, value='0').place(x=60, y=200)
    Radiobutton(root, text='High     (✭✭✭)', variable=radio_rhythm, value='2').place(x=60, y=220)
    Radiobutton(root, text='Low      (✭)', variable=radio_rhythm, value='1').place(x=60, y=240)

    ### comboboxMode Mode
    # label_2 = tk.Label(root,text='Mode').place(x=10, y=300)

    # comboboxMode = ttk.Combobox(root, width =10)
    # comboboxMode.place(x=70, y=300)
    # comboboxMode['state'] = ['readonly']
    # comboboxMode['values'] = ['Listen','Practice','Play']
    # Default_Listen = comboboxMode.set('Listen')

    ### comboboxMode Tonality
    label_3 = tk.Label(root,text='Tonality').place(x=10, y=340) 

    comboboxTona = ttk.Combobox(root, width =10)
    comboboxTona.place(x=70, y=340)
    comboboxTona['state'] = ['readonly']
    comboboxTona['values'] = ['C','G','D','A','E','F','Bb','Eb','Ab']

    ### scale tempo
    label_4 = tk.Label(root,text='Speed').place(x=10, y=390)

    var = DoubleVar()
    scale = Scale( root, variable = var, orient=HORIZONTAL,from_=40, to=200,activebackground = 'magenta', foreground = 'blue')
    scale.place(x=70, y=370)

    ### keyboard picture
    # keyboard = PhotoImage(file = 'keyboard.gif')
    # label_keyboard = Label(image = keyboard)
    # label_keyboard.place(x=130,y=620)
    # label_keyboard.image = keyboard # keep a reference!

    ### button OK, Play
    buttonOK = tk.Button(root, relief='flat', text='OK!', width=10, command = buttonOKClicked)
    buttonOK.place(x=40, y=450)

    # buttonPlay = tk.Button(root, relief='flat', text='Play !!!', width=10, command = buttonPlayClicked)
    # buttonPlay.place(x=40, y=490)

    # buttonStop = tk.Button(root, relief='flat', text='Stop', width=10, command = buttonStopClicked)
    # buttonStop.place(x=40, y=530)

    # Create the Menu 
    menubar = Menu(root)

    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Sample 1", command=openSample1)
    editmenu.add_command(label="Sample 2", command=openSample2)
    menubar.add_cascade(label="Sample",menu=editmenu)
    
    root.config(menu=menubar)

### main loop
if __name__ == '__main__':
    print('hello world') 

    root = Tk()
    root.title('Hello!!!')

    # root.bind('<KeyPress>', onKeyPress)

    main()
    mainloop()