import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

import for_sheet
import for_modify
import time

import for_metronome
import for_line

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

import buttom_Play
# import mtTkinter as Tkinter
# from mtTkinter import *
# import mtTkinter as Tkinter

import for_change

global note_x
note_x = []

global w


def __call__(self, *args, **kwargs):
    return self.decorator(self.func)(*args, **kwargs)

def savefile():
    labelHello.config(text = 'save the file: -change.xml')

def about():
    print('This is about simplify sheet')

def hello():
    print('hello')

def openfile():
    
    global filename
    filename = root.fileName = filedialog.askopenfilename( filetypes = (("Musicxml","*.xml"),("midi file","*.mid")))
    print(root.fileName)

    # global change_temp
    # change_temp = open('change-temp.xml','w')

    global Default_Tona

    ### for-parsing
    ### default tonalite and tempo
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    a = for_parsing.parsing(collection ,note_x)
    # print('open file note_x :', note_x) 
    # print('len note_x: ', len(note_x))
    ### a = (fifths, per_minute)
    ### a[0] = fifths
    ### a[1] = per_minute

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

    scale.set(a[1])

    labelHello.config(text = 'Choose the Simplify, Mode, Tonality and speed')


def openSample():

    # global change_temp
    # change_temp = open('change-temp.xml','w')

    global Default_Tona

    global filename

    DOMTree = xml.dom.minidom.parse('two-hand-2.xml')
    collection = DOMTree.documentElement
    
    a = for_parsing.parsing(collection, note_x)
    # print('note_x :', note_x) 
    # print(a)

    ### a = (fifths, per_minute)
    ### a[0] = fifths
    ### a[1] = per_minute

    filename = 'two-hand-2.xml'

    labelHello.config(text = 'Choose the Simplify, Mode, Tonality and speed')
    
    ### default tonalite and tempo
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

    scale.set(a[1])

def buttomOKClicked():

    Mode = Tona = Tem = ''

    ### simple
    # print('get Mode (Daul, Rhythm, Accent): ',checklist())
    print("Daul: ",var1.get(), "Rhythm: ",var2.get(), "Accent: ",var3.get())
    
    rhythm = var2.get()
    # print('rhythm: ',rhythm)
    if(rhythm == 1):
        for_modify.simple_rhythm(filename)
    
    accent = var3.get()
    # print('accent: ',accent)
    if(accent == 1):
        for_modify.simple_accent(filename)
    
    daul = var1.get()
    # print('daul: ',daul)
    if(daul == 1):
        for_modify.simple_daul(filename, accent)

    ### mode
    Mode = comboboxMode.get()
    print('get Mode: ',Mode)
    
    ### Tonality
    Tona = comboboxTona.get()

    print('get Tona: ',Tona)
    for_modify.change_Tona(filename, Tona, accent, daul)

    ### tempo
    Tem = var.get()
    print('get Tem: ',Tem)
    
    for_modify.change_tempo(filename, str(Tem), accent, daul, Tona)

    
    ########### change all - 
    # for_change.change_temp(filename, daul, rhythm, accent, Default_Tona, Tona, Tem)
    # print('daul, rhythm, accent, Mode, Tona, Tem:' ,daul, rhythm, accent, Mode, Tona, Tem)



def buttomPlayClicked():

    # print('note_x :', note_x) 
    
    Li = 0
    Pr = 0
    Pl = 0

    Tem = var.get()
    # for_modify.change_tempo(filename,str(Tem))
    
    ### Mode - Listen
    if (comboboxMode.get() == 'Listen'):
        print('Listen')
        Li = 1
        labelHello.config(text = "Listen ")
        # for_line.continue_line(Tem,filename)
    
    ### Mode - Practice
    if (comboboxMode.get() == 'Practice'):
        Pr = 1
        # for_line.continue_line(Tem,filename)
        labelHello.config(text = "Practice ")

    ### Mode - Play
    if (comboboxMode.get() == 'Play'):
        Pl = 1
        # for_line.continue_line(Tem,filename)
        labelHello.config(text = "Play ")   

    buttom_Play.buttomPlay(filename ,Li, Pr, Pl, Tem, note_x)
    # print('note_x :', note_x) 

def checklist():
    print('aaa')
   # print("Daul: ",var1.get(), "Rhythm: ",var2.get(), "Accent: ",var3.get() )
   # Daul   = var1.get()
   # Rhythm = var2.get()
   # Accent = var3.get()
   # return (Daul,Rhythm,Accent)

# veiw.pack()
if __name__ == '__main__':

    print('hello world') 

    root = Tk()
    root.title('Hello!!!')

    veiw = Label(root,width="180", height="46") 
    veiw.pack()


    w = Canvas(width = 910, height = 500, bg = 'yellow')
    w.place(x= 278 ,y=38)
    

    labelHello = tk.Label(root, text = "Choose the file ", height = 5, width = 80, fg = "blue")
    labelHello.place(x=0, y= 550)

    # Label(root, text="Your sex:")
    label_1 = tk.Label(root,text='Simplize: ').place(x=10, y=10)
    var1 = IntVar()
    Checkbutton(root, text="Daul", variable=var1).place(x=70,y=30)
    
    var2 = IntVar()
    Checkbutton(root, text="Rhythm", variable=var2).place(x=70,y=50)
    
    var3 = IntVar()
    Checkbutton(root, text="non-Accent", variable=var3).place(x=70,y=70)
    # Button(root, text='Show', command=var_states).place(x=10,y=70)

    label_2 = tk.Label(root,text='Mode').place(x=10, y=110)

    comboboxMode = ttk.Combobox(root, width =10)
    comboboxMode.place(x=70, y=110)
    comboboxMode['state'] = ['readonly']
    comboboxMode['values'] = ['Listen','Practice','Play']
    Default_Listen = comboboxMode.set('Listen')

    label_3 = tk.Label(root,text='Tonality').place(x=10, y=150) 

    comboboxTona = ttk.Combobox(root, width =10)
    comboboxTona.place(x=70, y=150)
    comboboxTona['state'] = ['readonly']
    comboboxTona['values'] = ['C','D','E','F','G','A','B']

    label_4 = tk.Label(root,text='Speed').place(x=10, y=200)

    var = DoubleVar()
    scale = Scale( root, variable = var, orient=HORIZONTAL,from_=40, to=160,activebackground = 'magenta', foreground = 'blue')
    scale.place(x=65, y=180)

    keyboard = PhotoImage(file = 'keyboard.gif')
    label_keyboard = Label(image = keyboard)
    label_keyboard.place(x=130,y=620)
    label_keyboard.image = keyboard # keep a reference!

    buttomOK = tk.Button(root, relief='flat', text='OK!', width=10, command = buttomOKClicked)
    buttomOK.place(x=20, y=280)

    buttomPlay = tk.Button(root, relief='flat', text='Play !!!', width=10, command = buttomPlayClicked)
    buttomPlay.place(x=20, y=320)

    # Create the next the row down Edit
    menubar = Menu(root)

    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Sample 1", command=openSample)
    editmenu.add_command(label="Sample 2", command=hello)
    editmenu.add_command(label="Sample 3", command=hello)
    menubar.add_cascade(label="Sample",menu=editmenu)
    
    root.config(menu=menubar)

    # w.create_line(0, 0, 10, 500)

    mainloop()