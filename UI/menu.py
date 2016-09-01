### import tk
import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

### import time
import time

### import ElementTree for parsing 
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element



### import keyboard and thread
from threading import Thread
import sys, pygame, pygame.midi, time
from pygame.locals import *

'''
import all the function 

for_parsing - parse
for_sheet- draw the sheet
buttom_Play - when the Play button is click
'''
import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

from for_sheet import key_location, create_notes
import for_modify

import buttom_Play


### all the notes's x location. is str
global note_x
note_x = []

### w is the canvas
global w

### all notes's MIDI, X location, Y location. is str
global MIDI_str, key_x_str, key_y_str

MIDI_str = []
key_x_str = []
key_y_str = []

### global hands
global hands

### def function __call__
def __call__(self, *args, **kwargs):
    return self.decorator(self.func)(*args, **kwargs)

### def function hello for test
def hello():
    print('hello')

### def function open the file
def openfile():
    
    w.delete('all')
    ### file name is global
    global filename
    
    ### choose the file named '*.mid' & '*.xml'
    filename = root.fileName = filedialog.askopenfilename( filetypes = (("Musicxml","*.xml"),("midi file","*.mid")))
    print(root.fileName)

    ### Default_Tona is global
    global Default_Tona

    global hands

    hands = 0

    '''
    parsing the xml file and default tonalite and tempo
    
    note_x is all the notes' location
    
    a = (fifths, per_minute)
    a[0] = fifths
    a[1] = per_minute

    MIDI_str & notes x,y location  
    '''
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    a = for_parsing.parsing(w, collection ,note_x, MIDI_str, key_x_str, key_y_str, hands)

    ### Default_Tona
    if (a[0] == '0'):
        Default_Tona = comboboxTona.set('C')
    if (a[0] == '1'):
        Default_Tona = comboboxTona.set('G')
    if (a[0] == '2'):
        Default_Tona = comboboxTona.set('D')
    if (a[0] == '3'):
        Default_Tona = comboboxTona.set('A')
    if (a[0] == '4'):
        Default_Tona = comboboxTona.set('E')
    if (a[0] == '5'):
        Default_Tona = comboboxTona.set('B')
    if (a[0] == '6'):
        Default_Tona = comboboxTona.set('F')

    if (a[0] == '-1'):
        Default_Tona = comboboxTona.set('F')
    if (a[0] == '-2'):
        Default_Tona = comboboxTona.set('B')
    if (a[0] == '-3'):
        Default_Tona = comboboxTona.set('E')
    if (a[0] == '-4'):
        Default_Tona = comboboxTona.set('A')
    if (a[0] == '-5'):
        Default_Tona = comboboxTona.set('D')
    if (a[0] == '-6'):
        Default_Tona = comboboxTona.set('G')

    ### default tempo
    scale.set(a[1])

def openSample():
    w.delete('all')
    ### Unkown
    # global Default_Tona

    ### open Sample - global file name
    global filename
    filename = 'two-hand-2.xml'

    global hands

    hands = 0
    '''
    parsing the file named 'two-hand-2.xml' 
    
    note_x is all the notes' location
    
    a = (fifths, per_minute)
    a[0] = fifths
    a[1] = per_minute

    MIDI_str & notes x,y location  
    '''
    DOMTree = xml.dom.minidom.parse('two-hand-2.xml')
    collection = DOMTree.documentElement
    
    a = for_parsing.parsing(w, collection, note_x, MIDI_str, key_x_str, key_y_str, hands)
    
    ### Default_Tona
    if (a[0] == '0'):
        Default_Tona = comboboxTona.set('C')
    if (a[0] == '1'):
        Default_Tona = comboboxTona.set('G')
    if (a[0] == '2'):
        Default_Tona = comboboxTona.set('D')
    if (a[0] == '3'):
        Default_Tona = comboboxTona.set('A')
    if (a[0] == '4'):
        Default_Tona = comboboxTona.set('E')
    if (a[0] == '5'):
        Default_Tona = comboboxTona.set('B')
    if (a[0] == '6'):
        Default_Tona = comboboxTona.set('F')

    if (a[0] == '-1'):
        Default_Tona = comboboxTona.set('F')
    if (a[0] == '-2'):
        Default_Tona = comboboxTona.set('B')
    if (a[0] == '-3'):
        Default_Tona = comboboxTona.set('E')
    if (a[0] == '-4'):
        Default_Tona = comboboxTona.set('A')
    if (a[0] == '-5'):
        Default_Tona = comboboxTona.set('D')
    if (a[0] == '-6'):
        Default_Tona = comboboxTona.set('G')

    ### default tempo
    scale.set(a[1])

### def function OK button
def buttonOKClicked():
    w.delete('all')

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

    

### def functuin the button Play
def buttonPlayClicked():
    
    ## if(change_hands == 1):
        ## print('hands1111: ', change_hands)

    ### Mode Listen, Practice, Play = 0
    Li = 0
    Pr = 0
    Pl = 0

    ### get the Tem 
    Tem = var.get()
    
    '''
    get the Mode Listen or Practice or Play

    call the buttomPlay funtion 
    from ouside file named buttom_Play 
    file name, ,Listen value, Pratice value, Play value, Tempo, note_x, key_x_str, key_y_str
    '''
    if (comboboxMode.get() == 'Listen'):
        Li = 1
    if (comboboxMode.get() == 'Practice'):
        Pr = 1
    if (comboboxMode.get() == 'Play'):
        Pl = 1

    ### call the function named buttomPlay from the file named buttom_Play
    ### 'change_hands' is very importand


    # global w
    # w = Canvas(width = 910, height = 500, bg = 'yellow')
    # w.place(x= 278 ,y=8)

    buttom_Play.buttomPlay(w, filename ,Li, Pr, Pl, Tem, note_x, key_x_str, key_y_str, change_hands, MIDI_str)

### def main menu
def main():

    ### global all the event
    global labelHello, label_1, label_2, label_3, label_4, label_keyboard
    global comboboxMode, comboboxTona, scale, var1, var2, var3, var, radio_hand, radio_level

    ### labal
    veiw = Frame(root,width="1800", height="800") 
    # veiw.grid(row=0,column=0)
    veiw.pack()

    # ### big bug is here
    # canvas=Canvas(veiw, bg='yellow', width=1030, height=600, scrollregion=(0,0,300,300))
    
    # vbar=Scrollbar(veiw,orient=VERTICAL)
    # vbar.pack(side=RIGHT,fill=Y)
    # vbar.config(command=canvas.yview)
    # # canvas.config(width=1420,height=600)
    # canvas.place(x= 180 ,y=8)    
    # canvas.pack(side=RIGHT,expand=True,fill=BOTH)

    global w
    ### w = Canvas
    # w = Canvas(width = 1100, height = 570, bg = 'yellow')
    # w.place(x= 265 ,y=36)

    w = Canvas(width = 1100, height = 605)# , bg = 'yellow')
    w.place(x= 265 ,y=1)

    ### labelHello define
    # labelHello = tk.Label(root, text = "Choose the file ", height = 5, width = 80, fg = "blue")
    # labelHello.place(x=0, y= 550)

    # Checkbutton - Daul (var1), Rhythm (var2), Accent (var3)
    var1 = IntVar()
    Checkbutton(root, text="Daul", variable=var1).place(x=70,y=30)
    
    var2 = IntVar()
    # Checkbutton(root, text="Rhythm", variable=var2).place(x=70,y=50)
    
    var3 = IntVar()
    Checkbutton(root, text="Rhythm", variable=var3).place(x=70,y=50)

    ### radio for right or left hand
    radio_hand = IntVar()
    Radiobutton(root, text='Both Hands', variable=radio_hand, value='0').place(x=30, y=110)
    Radiobutton(root, text='Only Right Hand', variable=radio_hand, value='1').place(x=30, y=130)
    Radiobutton(root, text='Only Left Hand', variable=radio_hand, value='2').place(x=30, y=150)

    ### radio for level
    radio_level = IntVar()
    # Radiobutton(root, text='Original', variable=radio_level, value='0').place(x=30, y=180)
    Radiobutton(root, text='High', variable=radio_level, value='2').place(x=30, y=200)
    Radiobutton(root, text='Low', variable=radio_level, value='1').place(x=30, y=220)


    ### comboboxMode Mode
    label_2 = tk.Label(root,text='Mode').place(x=10, y=310)

    comboboxMode = ttk.Combobox(root, width =10)
    comboboxMode.place(x=70, y=310)
    comboboxMode['state'] = ['readonly']
    comboboxMode['values'] = ['Listen','Practice','Play']
    Default_Listen = comboboxMode.set('Listen')

    ### comboboxMode Tonality
    label_3 = tk.Label(root,text='Tonality').place(x=10, y=350) 

    comboboxTona = ttk.Combobox(root, width =10)
    comboboxTona.place(x=70, y=350)
    comboboxTona['state'] = ['readonly']
    comboboxTona['values'] = ['C','D','E','F','G','A','B']

    ### scale tempo
    label_4 = tk.Label(root,text='Speed').place(x=10, y=400)

    var = DoubleVar()
    scale = Scale( root, variable = var, orient=HORIZONTAL,from_=40, to=160,activebackground = 'magenta', foreground = 'blue')
    scale.place(x=65, y=380)

    ### keyboard picture
    keyboard = PhotoImage(file = 'keyboard.gif')
    label_keyboard = Label(image = keyboard)
    label_keyboard.place(x=130,y=620)
    label_keyboard.image = keyboard # keep a reference!

    ### button OK, Play
    buttonOK = tk.Button(root, relief='flat', text='OK!', width=10, command = buttonOKClicked)
    buttonOK.place(x=20, y=480)

    buttonPlay = tk.Button(root, relief='flat', text='Play !!!', width=10, command = buttonPlayClicked)
    buttonPlay.place(x=20, y=520)

    # Create the Menu 
    menubar = Menu(root)

    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Sample 1", command=openSample)
    editmenu.add_command(label="Sample 2", command=hello)
    editmenu.add_command(label="Sample 3", command=hello)
    menubar.add_cascade(label="Sample",menu=editmenu)
    
    root.config(menu=menubar)


### main loop
if __name__ == '__main__':

    print('hello world') 

    root = Tk()
    root.title('Hello!!!')

    ### scroll bar
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill=Y )

    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for line in range(100):
       mylist.insert(END, "This is line number " + str(line))

    mylist.pack( side = RIGHT, fill = BOTH )
    scrollbar.config( command = mylist.yview )

    main()
    mainloop()