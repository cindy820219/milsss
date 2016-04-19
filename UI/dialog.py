
import tkinter as tk
from tkinter import *
import time

root = Tk()
root.title('Hello!!!')

veiw = Label(root,width="180", height="40")
veiw.pack()

# create the canvas, size in pixels
canvas = Canvas(width = 300, height = 200, bg = 'yellow')
# pack the canvas into a frame/form
canvas.place(x= 100 ,y=20)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
gif1 = PhotoImage(file = 'whole.gif')
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
for x in range(20,50):
    canvas.create_image(x, 10, image = gif1, tag = "pic")
    canvas.update()
     
    # 暂停0.05妙，然后删除图像
    time.sleep(0.025)
    canvas.delete("pic")
# run it ...

mainloop()
