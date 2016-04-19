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

'''
### for mido 
import mido
import operator
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
from mido import MidiFile, MetaMessage
'''

root = Tk()
root.title('Hello!!!')

### Scrollbar
# s = Scrollbar(root)
### Scrollbar

# veiw
veiw = Label(root,width="180", height="40")
# some.pack()

## label
labelHello = tk.Label(root, text = "Choose the file, difficulty, Mode, Tonality, speed ", height = 5, width = 80, fg = "blue")
# labelHello = tk.Label(root, text = "")
labelHello.pack()


## difficulty
'''label = tk.Label(root,text='difficulty')
label.pack(side = LEFT) 
'''

label_1 = tk.Label(root,text='Difficulty')
label_1.place(x=10, y=10) 

# ttk combobox difficult
comboboxDiff = ttk.Combobox(root, width =10)
comboboxDiff.place(x=70, y=10)
comboboxDiff['state'] = ['readonly']
comboboxDiff['values'] = ['Original','Easy','Middle','High']

# def dropdown():
#    c.event_generate('<Button-1>')
# b = Button(root, text='test', command=dropdown)
# b.pack()


## Mode
label_2 = tk.Label(root,text='Mode')
label_2.place(x=10, y=50) 

# ttk combobox Mode
comboboxMode = ttk.Combobox(root, width =10)
comboboxMode.place(x=70, y=50)
comboboxMode['state'] = ['readonly']
comboboxMode['values'] = ['Listen','Practice','Play']


## Tonality
label_3 = tk.Label(root,text='Tonality')
label_3.place(x=10, y=90) 

# ttk combobox Tonality
comboboxTona = ttk.Combobox(root, width =10)
comboboxTona.place(x=70, y=90)
comboboxTona['state'] = ['readonly']
comboboxTona['values'] = ['C','D','E','F','A','B']

## speed
label_4 = tk.Label(root,text='Speed')
label_4.place(x=10, y=130)

# ttk combobox tempo
comboboxTem = ttk.Combobox(root, width =10)
comboboxTem.place(x=70, y=130)
# comboboxTem['state'] = ['readonly']
comboboxTem['values'] = ['60','80','100','120']

### draw the keyboard ### 
keyboard = PhotoImage(file = 'keyboard.gif')
label_keyboard = Label(image = keyboard)
#label.grid(row = 3, column = 1, padx = 5, pady = 5)
label_keyboard.place(x=230,y=620)
label_keyboard.image = keyboard # keep a reference!

keyboard = PhotoImage(file = 'keyboard.gif')
label_keyboard = Label(image = keyboard)
#label.grid(row = 3, column = 1, padx = 5, pady = 5)
label_keyboard.place(x=600,y=620)
label_keyboard.image = keyboard # keep a reference!

# for_metronome.metronome()

## def click buttom OK
def buttomOKClicked():
    labelHello.config(text = "Upload..")
    #parsing the music sheet
    
    Diff = comboboxDiff.get()
    print('Diff: ',Diff)
    
    Mode = comboboxMode.get()
    print('Mode: ',Mode)
    
    Tona = comboboxTona.get()
    print('Tona: ',Tona)
    
    ### change tem
    Tem = comboboxTem.get()
    print('Tem: ',Tem)
    for_modify.change_tempo(filename,Tem)

    # creat the music sheet
    # for_sheet.create_sheet()
    
# ttk buttom OK
buttomOK = tk.Button(root, relief='flat', text='OK!', width=10, command = buttomOKClicked)

buttomOK.place(x=20, y=170)


#### About the Menu #### 
def hello():
    print('hello')

def openfile():
    labelHello.config(text = 'open the file')
    global filename
    filename = root.fileName = filedialog.askopenfilename( filetypes = (("Musicxml","*.xml"),("midi file","*.mid")))
    # print(x)
    print(root.fileName)

    ### for-parsing
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection)

def savefile():
    labelHello.config(text = 'save the file: new.xml')

def about():
    print('This is about simplify sheet')

menubar = Menu(root)

# the UP row down File, and then add they to the up menu
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Create the next the row down Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Sample 1", command=hello)
editmenu.add_command(label="Sample 2", command=hello)
editmenu.add_command(label="Sample 3", command=hello)
menubar.add_cascade(label="Sample",menu=editmenu)
 

# view the menu
root.config(menu=menubar)

veiw.pack()

# mianloop
mainloop()
