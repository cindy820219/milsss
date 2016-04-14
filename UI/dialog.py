
import tkinter as tk
from tkinter import *

root = Tk()
s = Scrollbar(root)
T = Text(root)

T.focus_set()
s.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)

#for i in range(40): 
#    T.insert(END, "This is line %d\n" % i)

mainloop()



'''
from tkinter import *

root = Tk()

def create_button_with_scoped_image():
    img = PhotoImage(file="4.gif")  # reference PhotoImage in local variable
    # img.place(x=100,y=100)

    button = Button(root, image=img)
    button.img = img
    button.grid()

create_button_with_scoped_image()

root.mainloop()
'''
