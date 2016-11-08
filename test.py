# import tkinter as tk
# from tkinter import *
# from tkinter import ttk, Tk, StringVar
# import PIL
# from PIL import ImageTk, Image


# ### work !!!
# # root = Tk()

# # image = Image.open('file.gif')
# # photo = ImageTk.PhotoImage(image)

# # label = Label(image = photo)
# # label.image = photo

# # label.pack()

# # root.mainloop()
# ### work !!!

# # from subprocess import call
# # call(["ls", "-l"])
# # call(["sudo" , "/Applications/MuseScore\ 2.app/Contents/MacOS/mscore", "/Users/BlueT/Desktop/milsss/UI/two-hand-2.xml", "-o", "/Users/BlueT/Desktop/milsss/UI/file111.png"])
# # call(["sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/two-hand-2.xml -o /Users/BlueT/Desktop/milsss/UI/file.png"])
# # sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/two-hand-2.xml -o /Users/BlueT/Desktop/milsss/UI/file.png


# import os
# # cmd = 'sudo /Applications/MuseScore\ 2.app/Contents/MacOS/mscore /Users/BlueT/Desktop/milsss/UI/two-hand-2.xml -o /Users/BlueT/Desktop/milsss/UI/file111.png'
# # os.system(cmd)


# root = Tk()
# # image = PhotoImage(file = 'test.gif')
# # label_notes = Label(image = image)
# # label_notes.place(x=0,y=0)
# # label_notes.image = image # keep a reference!

# # img = PhotoImage(file = 'file.png')
# # a = Label(root, image= img)
# # a.pack()


# ### load.show()
# # render = ImageTk.PhotoImage(load)

# # img = Label(image= render)
# # img.image = render
# # img.place(x=100, y=100)

# # load = Image.open('file.png')
# # photo = ImageTk.PhotoImage(load)

# # image_label= Label(root,image = photo)
# # image_label.place(x = 0,y= 0)


# # new = imafe.new('RGBA', (200,200),'white')
# # draw = ImageDraw.Draw()

# # print('size: ', load.size)
# # print('name: ', load.filename)


# # root.mainloop()


# # root.mainloop()



# # import pygame

# # # music = pyglet.resource.media('wav.wav')
# # import time

# # pygame.init()

# # pygame.mixer.music.load("wav.wav")
# # # pygame.mixer.music.load("file.mid")

# # pygame.mixer.music.play()

# # time.sleep(3)







# ############################################
# #!/usr/bin/python3

# import _thread
# import time
# ### for pygame and play wav
# import pygame

# pygame.init()
# # 为线程定义一个函数
# def print_time( threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print( threadName)


#     print('in the thread!!!!!')

    
#     pygame.mixer.music.load("wav.wav")

#     pygame.mixer.music.play()
#     time.sleep(10)


# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )

# except:
#    print ("Error: cant start the thread!")

# while 1:
#    pass
############################################
#!/bin/env python
from tkinter import * 
from PIL import Image, ImageTk 

root = Tk()

image = Image.open("test-file-1.png")
photo = ImageTk.PhotoImage(image)
image_label = Label(root, width = 400, height = 400, image = photo)
# image.show()

root.mainloop()


# from tkinter import *


# root = Toplevel()

# im = PIL.Image.open("test-file-1.png")
# photo = PIL.ImageTk.PhotoImage(im)

# label = Label(root, image=photo)
# label.image = photo  # keep a reference!
# label.pack()

# root.mainloop()