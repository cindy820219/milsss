import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import PIL
from PIL import ImageTk, Image


### work !!!
# root = Tk()

# image = Image.open('file.gif')
# photo = ImageTk.PhotoImage(image)

# label = Label(image = photo)
# label.image = photo

# label.pack()

# root.mainloop()
### work !!!

# from subprocess import call
# call(["ls", "-l"])
# call(["sudo" , "/Applications/MuseScore\ 2.app/Contents/MacOS/mscore", "/Users/BlueT/Desktop/milsss/UI/two-hand-2.xml", "-o", "/Users/BlueT/Desktop/milsss/UI/file111.png"])
# call(["sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/two-hand-2.xml -o /Users/BlueT/Desktop/milsss/UI/file.png"])
# sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/two-hand-2.xml -o /Users/BlueT/Desktop/milsss/UI/file.png


import os
# cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/two-hand-2.xml -o /Users/BlueT/Desktop/milsss/UI/file111.png'
# os.system(cmd)


root = Tk()
# image = PhotoImage(file = 'test.gif')
# label_notes = Label(image = image)
# label_notes.place(x=0,y=0)
# label_notes.image = image # keep a reference!

img = PhotoImage(file = 'file.png')
a = Label(root, image= img)
a.pack()


### load.show()
# render = ImageTk.PhotoImage(load)

# img = Label(image= render)
# img.image = render
# img.place(x=100, y=100)

# load = Image.open('file.png')
# photo = ImageTk.PhotoImage(load)

# image_label= Label(root,image = photo)
# image_label.place(x = 0,y= 0)


print('size: ', load.size)
print('name: ', load.filename)


root.mainloop()


# root.mainloop()