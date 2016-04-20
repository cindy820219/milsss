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

def buttomOKClicked():

    Mode = Tona = Tem = ''

    Mode = comboboxMode.get()
    print('get Mode: ',Mode)
    
    Tona = comboboxTona.get()
    print('get Tona: ',Tona)

    Tem = var.get()
    print('get Tem: ',Tem)
    for_modify.change_tempo(filename,str(Tem))
    labelHello.config(text = "Upload")

    for_modify.change_Tona(filename,Tona)

def buttomPlayClicked():
    Tem = var.get()
    # for_modify.change_tempo(filename,str(Tem))

    for_line.red_line(Tem)
    labelHello.config(text = "play ")

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

def savefile():
    labelHello.config(text = 'save the file: -change.xml')

def about():
    print('This is about simplify sheet')

# veiw.pack()
if __name__ == '__main__':
    print('hello world') 

    root = Tk()
    root.title('Hello!!!')

    veiw = Label(root,width="180", height="46") 
    veiw.pack()

    labelHello = tk.Label(root, text = "Choose the file ", height = 5, width = 80, fg = "blue")
    labelHello.place(x=0, y= 550)


    daul_IntVar = IntVar()
    tempo_IntVar = IntVar()
    retake_IntVar = IntVar()

    daul = Checkbutton(root, text="Simplize Daul", variable=daul_IntVar)
    tempo = Checkbutton(root, text="Simplize Rhythm", variable=tempo_IntVar)
    retake = Checkbutton(root, text="Simplize ...", variable=retake_IntVar)

    daul.var = daul_IntVar
    tempo.var = tempo_IntVar
    retake.var = retake_IntVar

    daul.place(x=10, y=30)
    tempo.place(x=10, y=50)
    retake.place(x=10, y=70)

    label_2 = tk.Label(root,text='Mode')
    label_2.place(x=10, y=110) 

    comboboxMode = ttk.Combobox(root, width =10)
    comboboxMode.place(x=70, y=110)
    comboboxMode['state'] = ['readonly']
    comboboxMode['values'] = ['Listen','Practice','Play']

    label_3 = tk.Label(root,text='Tonality')
    label_3.place(x=10, y=150) 

    comboboxTona = ttk.Combobox(root, width =10)
    comboboxTona.place(x=70, y=150)
    comboboxTona['state'] = ['readonly']
    comboboxTona['values'] = ['C','D','E','F','A','B']

    label_4 = tk.Label(root,text='Speed')
    label_4.place(x=10, y=200)

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
    editmenu.add_command(label="Sample 1", command=hello)
    editmenu.add_command(label="Sample 2", command=hello)
    editmenu.add_command(label="Sample 3", command=hello)
    menubar.add_cascade(label="Sample",menu=editmenu)
    
    root.config(menu=menubar)

    mainloop()
