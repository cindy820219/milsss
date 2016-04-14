import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

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

def service_fun():
    print('this is service_fun ~~~~~~')

def create_sheet():
    photo = PhotoImage(file = '4.gif')
    label_sheet = Label(image = photo)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_sheet.place(x=200,y=80)
    label_sheet.image = photo # keep a reference!

    photo = PhotoImage(file = '4.gif')
    label_sheet = Label(image = photo)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_sheet.place(x=200,y=280)
    label_sheet.image = photo # keep a reference!

    photo = PhotoImage(file = '4.gif')
    label_sheet = Label(image = photo)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_sheet.place(x=200,y=480)
    label_sheet.image = photo # keep a reference!

    # quarter
    quarter = PhotoImage(file = 'quarter.gif')
    label_notes = Label(image = quarter)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_notes.place(x=300,y=100)
    label_notes.image = quarter # keep a reference!

    # whole
    whole = PhotoImage(file = 'whole.gif')
    label_notes = Label(image = whole)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_notes.place(x=340,y=100)
    label_notes.image = whole # keep a reference!

    # eight
    eight = PhotoImage(file = 'eight.gif')
    label_notes = Label(image = eight)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_notes.place(x=380,y=100)
    label_notes.image = eight # keep a reference!

    # six
    six = PhotoImage(file = '16th.gif')
    label_notes = Label(image = six)
    #label.grid(row = 3, column = 1, padx = 5, pady = 5)
    label_notes.place(x=420,y=100)
    label_notes.image = six # keep a reference!v

## def click buttom OK
def buttomOKClicked():
    labelHello.config(text = "Upload..")
    #parsing the music sheet

    # creat the music sheet
    create_sheet()
    
# ttk buttom OK
buttomOK = tk.Button(root, relief='flat', text='OK!', width=10, command = buttomOKClicked)

buttomOK.place(x=20, y=170)


## radio check 單選選項
# def colorChecked():
#     labelHello.config(fg = color.get())

# color = tk.StringVar()
# tk.Radiobutton(root, text = "Listen", value = "red").pack(side = tk.LEFT)
# tk.Radiobutton(root, text = "Practice", value = "blue").pack(side = tk.LEFT)
# tk.Radiobutton(root, text = "Play", value = "green").pack(side = tk.LEFT)

## type check 複選選項
# def typeChecked():
#         textType = typeBlod.get() + typeItalic.get()
#         if textType == 1:
#                 labelHello.config(font = ("Arial", 12, "bold"))
#         elif textType == 2:
#                 labelHello.config(font = ("Arial", 12, "italic"))
#         elif textType == 3:
#                 labelHello.config(font = ("Arial", 12, "bold italic"))
#         else :
#                 labelHello.config(font = ("Arial", 12))

# typeBlod = tk.IntVar()
# typeItalic = tk.IntVar()
# tk.Checkbutton(root, text = "one", variable = typeBlod, onvalue = 1, offvalue = 0, command = typeChecked).pack(side = tk.LEFT)
# tk.Checkbutton(root, text = "two", variable = typeItalic, onvalue = 2, offvalue = 0, command = typeChecked).pack(side = tk.LEFT)


#### About the Menu #### 

def hello():
    print('hello')

def openfile():
    labelHello.config(text = 'open the file')
    x = root.fileName = filedialog.askopenfilename( filetypes = (("Musicxml","*.xml"),("midi file","*.mid")))
    # print(x)
    print(root.fileName)

    ### for-parsing
    DOMTree = xml.dom.minidom.parse(x)
    collection = DOMTree.documentElement
    for_parsing.parsing(collection)

    # service_fun()
    # for_parsing.some_fun()


    # doparsing()
    '''
    i = 0
    mid = MidiFile('two-hand-2.xml')
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for message in track:
            i=i+1
            print(i,' ',message)
    '''

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
 
# # the row down : Help
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="About", command=about)
# menubar.add_cascade(label="Help", menu=helpmenu)

# view the menu
root.config(menu=menubar)

veiw.pack()

# mianloop
mainloop()
