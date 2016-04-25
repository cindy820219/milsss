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

# import mtTkinter as Tkinter
# from mtTkinter import *
# import mtTkinter as Tkinter


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

    ### for-parsing
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection)

    labelHello.config(text = 'Choose the Simplify, Mode, Tonality and speed')

def openSample():
    global filename

    DOMTree = xml.dom.minidom.parse('two-hand-2.xml')
    collection = DOMTree.documentElement
    for_parsing.parsing(collection)
    filename = 'two-hand-2.xml'

def buttomOKClicked():

    Mode = Tona = Tem = ''

    ### simple
    print('get Mode (Daul, Rhythm): ',checklist())
    daul = var1.get()
    # if(daul == 1):
        # for_modify.simple_daul(filename)
        # simple_daul(filename)

    ### Tonality
    Tona = comboboxTona.get()
    print('get Tona: ',Tona)

    ### tempo
    Tem = var.get()
    print('get Tem: ',Tem)
    
    for_modify.change_tempo(filename,str(Tem))
    for_modify.change_Tona(filename,Tona)
    


    
def buttomPlayClicked():
    Tem = var.get()
    # for_modify.change_tempo(filename,str(Tem))

    for_line.red_line(Tem)
    labelHello.config(text = "play ")

def checklist():
   # print("Daul: ",var1.get(), "Rhythm: ",var2.get())
   Daul = var1.get()
   Rhythm = var2.get()
   return (Daul,Rhythm)

# veiw.pack()
if __name__ == '__main__':

    print('hello world') 

    root = Tk()
    root.title('Hello!!!')

    veiw = Label(root,width="180", height="46") 
    veiw.pack()

    labelHello = tk.Label(root, text = "Choose the file ", height = 5, width = 80, fg = "blue")
    labelHello.place(x=0, y= 550)

    # Label(root, text="Your sex:")
    label_1 = tk.Label(root,text='Simplize: ').place(x=10, y=10)
    var1 = IntVar()
    Checkbutton(root, text="Daul", variable=var1).place(x=70,y=30)
    var2 = IntVar()
    Checkbutton(root, text="Rhythm", variable=var2).place(x=70,y=50)
    var3 = IntVar()
    Checkbutton(root, text="Accent", variable=var3).place(x=70,y=70)
    # Button(root, text='Show', command=var_states).place(x=10,y=70)

    label_2 = tk.Label(root,text='Mode').place(x=10, y=110)

    comboboxMode = ttk.Combobox(root, width =10)
    comboboxMode.place(x=70, y=110)
    comboboxMode['state'] = ['readonly']
    comboboxMode['values'] = ['Listen','Practice','Play']

    label_3 = tk.Label(root,text='Tonality').place(x=10, y=150) 

    comboboxTona = ttk.Combobox(root, width =10)
    comboboxTona.place(x=70, y=150)
    comboboxTona['state'] = ['readonly']
    comboboxTona['values'] = ['C','D','E','F','A','B']

    label_4 = tk.Label(root,text='Speed').place(x=10, y=200)

    var = DoubleVar()
    scale = Scale( root, variable = var, orient=HORIZONTAL,from_=40, to=160,activebackground = 'magenta', foreground = 'blue')
    scale.place(x=65, y=180)

    keyboard = PhotoImage(file = 'keyboard.gif')
    label_keyboard = Label(image = keyboard)
    label_keyboard.place(x=230,y=620)
    label_keyboard.image = keyboard # keep a reference!

    keyboard = PhotoImage(file = 'keyboard.gif')
    label_keyboard = Label(image = keyboard)
    label_keyboard.place(x=600,y=620)
    label_keyboard.image = keyboard 

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

    mainloop()
