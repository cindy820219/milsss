### import tk
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

from tkinter import messagebox

### import ElementTree for parsing 
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

from xml.dom.minidom import parse
import xml.dom.minidom

### import keyboard and thread
from threading import Thread
import _thread
import sys, pygame, pygame.midi, time
from pygame.locals import *

'''
import all the function 

for_parsing - parse
for_sheet- draw the sheet
buttom_Play - when the Play button is click
'''
import for_parsing
from for_sheet import key_location, create_notes
import for_modify
import buttom_Play


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
            fifths = key.getElementsByTagName('fifths')[0]
            fifths = fifths.childNodes[0].data
            print('key:' ,fifths)

        times = collection.getElementsByTagName('time')
        for time in times:
            beats = time.getElementsByTagName('beats')[0]
            beattype = time.getElementsByTagName('beat-type')[0]

            beats = beats.childNodes[0].data
            beattype = beattype.childNodes[0].data

            print('times: ',beats+'/'+beattype+' ')
            
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
            print('tempo: ',sound)


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
        Default_Tona = 'C'
        print('  is too difficult!')
    if (fifths == '6'):
        Default_Tona = 'C'
        print('  is too difficult!')

    if (fifths == '-1'):
        Default_Tona = 'F'
    if (fifths == '-2'):
        Default_Tona = 'Bb'
    if (fifths == '-3'):
        Default_Tona = 'Eb'
    if (fifths == '-4'):
        Default_Tona = 'Ab'
    if (fifths == '-5'):
        Default_Tona = 'C'
        print('  is too difficult!')
    if (fifths == '-6'):
        Default_Tona = 'C'
        print('  is too difficult!')

    # print('Default_Tona: ',Default_Tona)
    return(Default_Tona, per_minute)

def openSample1():
    print('open file : sonatina.xml')
    ### open XML with the MuseScore and save the file named : test-file.png
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/sonatina.xml -o /Users/nien/Desktop/milsss/UI/new_readxml.png'
    os.system(cmd)

    ### small 50% : test-file-1.png to small.png
    cmd = 'convert new_readxml-1.png -resize 40% new_small.png'
    os.system(cmd)

    ### turn the small.png to test-file-1.gif
    cmd = 'convert new_small.png new_readfilegif.gif'
    os.system(cmd)    

    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'new_readfilegif.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-140)
    label_image.image = image # keep a reference!

    ### turn the xml to wav
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/sonatina.xml -o /Users/nien/Desktop/milsss/UI/new_wav.wav'
    os.system(cmd)

    ### filename
    global filename
    filename = 'sonatina.xml'

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
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/sonatina.xml -o /Users/nien/Desktop/milsss/UI/new_readxml.png'
    os.system(cmd)

    ### small 50% : test-file-1.png to small.png
    cmd = 'convert new_readxml-1.png -resize 40% new_small.png'
    os.system(cmd)

    ### turn the small.png to test-file-1.gif
    cmd = 'convert new_small.png new_readfilegif.gif'
    os.system(cmd)    

    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'new_readfilegif.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-140)
    label_image.image = image # keep a reference!

    ### turn the xml to wav
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/sonatina.xml -o /Users/nien/Desktop/milsss/UI/new_wav.wav'
    os.system(cmd)

    ### filename
    global filename
    filename = 'sonatina2.xml'

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
    
    cmd = 'sudo '
    cmd1 = '/Applications/MuseScore\ 2.app/Contents/MacOS/mscore '
    cmd2 = filename
    cmd3 = ' -o /Users/nien/Desktop/milsss/UI/new_readxml.png'
    # print('aaaaa: ',cmd + cmd1  + cmd2 + cmd3)
    os.system(cmd + cmd1  + cmd2 + cmd3)

    ### small 50% : test-file-1.png to small.png
    cmd = 'convert new_readxml-1.png -resize 40% new_small.png'
    os.system(cmd)

    ### turn the small.png to test-file-1.gif
    cmd = 'convert new_small.png new_readfilegif.gif'
    os.system(cmd)  

    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'new_readfilegif.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-140)
    label_image.image = image # keep a reference!

    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement

    ### find the default
    default_tempo_tonation = default(collection)
    comboboxTona.set(default_tempo_tonation[0])
    scale.set(default_tempo_tonation[1])



### def function OK button
def buttonOKClicked():
    
    print('Default_Tona: ',Default_Tona)
    
    global filename

    ### default the Mode, Tonation and Tempo
    Mode = Tona = Tem = ''
    
    '''
    if both  hand, hands = 0
    if right hand, hands = 1
    if left  hand, hands = 1
    '''
    hands = 0

    ''' 
    check the file name and get Mode, Tonation and Tempo
    get rhythm from var2
    get accent from var3
    get daul   from var1
    '''
    print('filename: ', filename)
    print("Daul: ",var1.get(), "Accent: ",var3.get()) ###, "Rhythm: ",var2.get(), "Accent: ",var3.get())
    
    ### radio for level
    ### hight level = 2, low level = 1
    level = str(radio_level.get())
    print('level: ', level)


    rhythm = var2.get()
    # print('rhythm: ',rhythm)
    if(rhythm == 1):
        for_modify.simple_rhythm(filename)

    accent = var3.get()
    if(accent == 1):
       for_modify.simple_accent(w, filename, hands)
    
    daul = var1.get()
    if(daul == 1):
        for_modify.simple_daul(filename, accent, level)

    ### get Mode value
    Mode = comboboxMode.get()
    print('get Mode: ',Mode)
    

    '''
    get Tonality value

    call the change_Tona funtion 
    from ouside file named for_modify 
    file name, Tonation, Accent and daul 
    '''
    Tona = comboboxTona.get()
    print('get Tona: ',Tona)
    for_modify.change_Tona(filename, Tona, accent, daul)


    '''
    get Tempo value

    call the change_tempo funtion 
    from ouside file named for_modify 
    file name, Tempo, accent, daul, and tonation
    '''
    Tem = var.get()
    print('get Tem: ',Tem)
    for_modify.change_tempo(filename, str(Tem), accent, daul, Tona)
   

    ### radio for right or left hand
    # print('seletion: ', str(radio_hand.get()))
    hand = str(radio_hand.get())
    ### if only one hand, then call the funtion
    if(hand != '0'):
        hands = 1
        for_modify.hand(filename, hand, accent, daul, Tona)

    


    '''
    parsing the 'change-temp.xml' 
    and turn the file name to 'change-temp.xml' 
    '''
    DOMTree = xml.dom.minidom.parse('change-temp.xml')
    collection = DOMTree.documentElement
    # hand
    a = for_parsing.parsing(w, collection, note_x,  MIDI_str, key_x_str, key_y_str, hands)

    filename = 'change-temp.xml'
    
    ### external command line
    ### open XML with the MuseScore and save the file named : test-file.png
    ### sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/change-temp.xml -o /Users/BlueT/Desktop/milsss/UI/change-temp.png
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/change-temp.xml -o /Users/nien/Desktop/milsss/UI/change-temp.png'
    os.system(cmd)

    ### small 50% : test-file-1.png to small.png
    cmd = 'convert change-temp-1.png -resize 50% change-temp-small.png'
    os.system(cmd)

    ### turn the small.png to test-file-1.gif
    cmd = 'convert -delay 35 -loop 0 change-temp-small.png change-temp-1.gif'
    os.system(cmd)    


    # root = Tk()
    # image = PhotoImage(file = 'test.gif-file.gif')
    image = PhotoImage(file = 'change-temp-1.gif')
    label_image = Label(image = image)
    label_image.place(x=180,y=-160)
    label_image.image = image # keep a reference!


    ### turn the xml to wav
    cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/nien/Desktop/milsss/UI/change-temp.xml -o /Users/nien/Desktop/milsss/UI/wav.wav'
    os.system(cmd)


    ### if hands are two, then change hands = hands
    ### to mark the hands
    global change_hands
    change_hands = 0
    change_hands = hands
    # print('hands change: ', change_hands)

    # global w
    # ### w = Canvas
    # w = Canvas(width = 910, height = 500, bg = 'yellow')
    # w.place(x= 278 ,y=38)

    # dialog_title = 'Attention !'
    # dialog_text = 'Its finished :)'

    # answer = messagebox.askquestion(dialog_title, dialog_text)
    # if (answer == 'yes'):
    #     print('yoyoyo')





def main():
    ### global all the event
    global label_2, label_3, label_4, label_keyboard
    global comboboxMode, comboboxTona, scale, var1, var2, var3, var, radio_hand, radio_level

    ### labal
    veiw = Frame(root,width="1400", height="700") 
    # veiw.grid(row=0,column=0)
    veiw.pack()

    ### radio for right or left hand
    radio_hand = IntVar()
    Radiobutton(root, text='Both Hands', variable=radio_hand, value='0').place(x=30, y=40)
    Radiobutton(root, text='Only Right Hand', variable=radio_hand, value='1').place(x=30, y=60)
    Radiobutton(root, text='Only Left Hand', variable=radio_hand, value='2').place(x=30, y=80)

    # Checkbutton - Daul (var1), Rhythm (var2), Accent (var3)
    var1 = IntVar()
    Checkbutton(root, text="Dual", variable=var1).place(x=30,y=140)
    
    var2 = IntVar()
    # Checkbutton(root, text="Rhythm", variable=var2).place(x=70,y=50)
    
    var3 = IntVar()
    Checkbutton(root, text="Rhythm", variable=var3).place(x=30,y=170)

    
    ### radio for level
    radio_level = IntVar()
    # Radiobutton(root, text='Original', variable=radio_level, value='0').place(x=30, y=180)
    Radiobutton(root, text='original', variable=radio_level, value='0').place(x=110, y=130)
    Radiobutton(root, text='High', variable=radio_level, value='2').place(x=110, y=150)
    Radiobutton(root, text='Low', variable=radio_level, value='1').place(x=110, y=170)

    ### comboboxMode Mode
    label_2 = tk.Label(root,text='Mode').place(x=10, y=250)

    comboboxMode = ttk.Combobox(root, width =10)
    comboboxMode.place(x=70, y=250)
    comboboxMode['state'] = ['readonly']
    comboboxMode['values'] = ['Listen','Practice','Play']
    Default_Listen = comboboxMode.set('Listen')

    ### comboboxMode Tonality
    label_3 = tk.Label(root,text='Tonality').place(x=10, y=290) 

    comboboxTona = ttk.Combobox(root, width =10)
    comboboxTona.place(x=70, y=290)
    comboboxTona['state'] = ['readonly']
    comboboxTona['values'] = ['C','G','D','A','E','F','Bb','Eb','Ab']

    ### scale tempo
    label_4 = tk.Label(root,text='Speed').place(x=10, y=340)

    var = DoubleVar()
    scale = Scale( root, variable = var, orient=HORIZONTAL,from_=40, to=200,activebackground = 'magenta', foreground = 'blue')
    scale.place(x=70, y=320)

    ### keyboard picture
    # keyboard = PhotoImage(file = 'keyboard.gif')
    # label_keyboard = Label(image = keyboard)
    # label_keyboard.place(x=130,y=620)
    # label_keyboard.image = keyboard # keep a reference!

    ### button OK, Play
    buttonOK = tk.Button(root, relief='flat', text='OK!', width=10, command = buttonOKClicked)
    buttonOK.place(x=40, y=450)

    # buttonPlay = tk.Button(root, relief='flat', text='Play !!!', width=10, command = buttonPlayClicked)
    # buttonPlay.place(x=20, y=520)

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

    main()
    mainloop()