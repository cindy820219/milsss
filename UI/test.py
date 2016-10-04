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

root = Tk()
image = PhotoImage(file = 'file.gif')
label_notes = Label(image = image)
label_notes.place(x=0,y=0)
label_notes.image = image # keep a reference!

root.mainloop()



# root = Tk()

# photo = PhotoImage(file='file.gif')
# photo_label = Label(image=photo)
# photo_label.grid()
# photo_label.image = photo_label

# root.mainloop()