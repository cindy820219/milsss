import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar

### for mido 
import mido
import operator
from mido import Message
from mido.midifiles import MidiFile, MidiTrack
from mido import MidiFile, MetaMessage


root = Tk()
root.title('Hello!!!')

# veiw
veiw = Label(root,width="120", height="40")
# some.pack()

## label
labelHello = tk.Label(root, text = "Choose the mode", height = 5, width = 80, fg = "blue")
labelHello.pack()

## 難易度
label = tk.Label(root,text='難易度')
label.pack(side = LEFT) 

# ttk combobox difficult
comboboxDiff = ttk.Combobox(root)
comboboxDiff.pack(side = LEFT)
comboboxDiff['state'] = ['readonly']
comboboxDiff['values'] = ['Original','Easy','Middle','High']

# def dropdown():
#    c.event_generate('<Button-1>')
# b = Button(root, text='test', command=dropdown)
# b.pack()


## 模式
label = tk.Label(root,text='模式')
label.pack(side = LEFT)

# ttk combobox Mode
comboboxMode = ttk.Combobox(root)
comboboxMode.pack(side = LEFT)
comboboxMode['state'] = ['readonly']
comboboxMode['values'] = ['Listen','Practice','Play']


## 調性
label = tk.Label(root,text='調性')
label.pack(side = tk.LEFT)

# ttk combobox Tonality
comboboxTona = ttk.Combobox(root)
comboboxTona.pack(side = LEFT)
comboboxTona['state'] = ['readonly']
comboboxTona['values'] = ['C','D','E','F','A','B']

## 速度
label = tk.Label(root,text='速度')
label.pack(side = LEFT)

# ttk combobox tempo
comboboxTem = ttk.Combobox(root)
comboboxTem.pack(side = LEFT)
comboboxTem['values'] = ['60','80','100','120']

## def click buttom OK
def buttomOKClicked():
	labelHello.config(text = "Upload..")

# ttk buttom OK
buttomOK = tk.Button(root, 
                relief='flat',
                text='OK!',
                width=10,
                command = buttomOKClicked)
buttomOK.pack(side = LEFT)


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


#### About the Menu ###
def hello():
	print('hello')

#def txtRead():
#	print('hello')
#	file = open("do.txt", "r")
	# print(file)
	# print(type(file))
#	print(file.readline())

def openfile():
	labelHello.config(text = 'open the file: midi-only')
	i = 0
	mid = MidiFile('midi-only.mid')
	for i, track in enumerate(mid.tracks):
		print('Track {}: {}'.format(i, track.name))
		for message in track:
			i=i+1
			print(i,' ',message)

def savefile():
	labelHello.config(text = 'save the file: midi-new-only')

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