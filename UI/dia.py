import tkinter as tk
from tkinter import *
from tkinter import ttk, Tk, StringVar
import tkinter.filedialog as filedialog

import for_parsing
from xml.dom.minidom import parse
import xml.dom.minidom

root = Tk()
root.title('Hello!!!')
veiw = Label(root,width="180", height="46") 
veiw.pack()

w = Canvas(width = 910, height = 500, bg = 'yellow')
w.place(x= 278 ,y=38)


'''
w = Canvas(width = 910, height = 50) #,bg = 'yellow')
w.place(x= 278 ,y=38)
w.create_line(0, 2.5, 910, 2.5)
'''

sh = PhotoImage(file = '3u6.gif')
w.create_image(0,0,image = sh) 

im = PhotoImage(file = 'half.gif')
w.create_image(300,30,image = im) 

mainloop()