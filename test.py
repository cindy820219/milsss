from tkinter import *          

# photo = PhotoImage(file= PhotoImage(file='/Users/nien/Desktop/milsss/sonatina2.png'))


# from Tkinter import *
import PIL.Image
import PIL.ImageTk

root = Toplevel()

im = PIL.Image.open("sonatina2.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

root.mainloop()