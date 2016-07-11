### for tk, ttk and filedialog
from tkinter import *
import tkinter.filedialog as filedialog
from tkinter import ttk, Tk, StringVar

### midi-keybroad and pygame
import sys, pygame, pygame.midi, time
from pygame.locals import *

# creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

        self.Checkbutton()

        self.Combo_mode()
        self.Combo_tona()

        # self.right_dot()
        # self.MIDI_note()

    ###### Checkbutton ###### 
    def Checkbutton(self):
        self.var_daul = IntVar()
        daul = Checkbutton(self.master, text="Daul", variable=self.var_daul)#, command=self.cb_daul)
        daul.place(x=30, y=10)

        self.var_rhythm = IntVar()
        rhythm = Checkbutton(self.master, text="Rhythm", variable=self.var_rhythm)#, command=self.cb_rhythm)
        rhythm.place(x=30, y=30)

    ###### Combo ######
    # mode combo
    def Combo_mode(self):
        self.box_mode = StringVar()
        self.box = ttk.Combobox(self.master, textvariable=self.box_mode, state='readonly', width =10)
        self.box['values'] = ('Listen','Practice','Play')
        self.box.current(0)
        self.box.place(x=30, y =90)

    # tonation combo
    def Combo_tona(self):
        self.box_tona = StringVar()
        self.box = ttk.Combobox(self.master, textvariable=self.box_tona, state='readonly', width =10)
        self.box['values'] = ('C','D','E','F','G','A','B')
        self.box.current(0)
        self.box.place(x=30, y =130)


    ###### Creation of init_window --- menu
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("MusicXml")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)
        
        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        # file add 'Open'
        file.add_command(label="Open", command=self.openfile)
        # file separator line
        file.add_separator()
        # file add 'Exit'
        file.add_command(label="Exit", command=self.client_exit)

        # create the file object 'sample' in menu
        Sample = Menu(menu)
        # Sample add 'Sample 1'
        Sample.add_command(label="Sample 1")
        # Sample add 'Sample 2'
        Sample.add_command(label="Sample 2")
        #added "file" to our menu
        menu.add_cascade(label="Sample", menu=Sample)

        ###### creat canvas //it sift 200 to left
        canvas = Canvas(self, width = 1350, height = 750, bg = 'yellow',borderwidth=0,
           highlightthickness=0,)
        canvas.place(x=78 ,y=8)

        ###### scale speed ######
        self.var = IntVar()
        self.scale = Scale(self, from_=40, to=160, orient=HORIZONTAL, activebackground = 'magenta', foreground = 'blue') #, command=self.onScale)
        self.scale.place(x=30, y =170)
        
        ###### button OK! ######
        self.OK = Button(self)
        self.OK['text'] = 'OK !'
        self.OK['command'] = self.OKOK
        self.OK.place(x=30, y =240)

        ###### button Play! ######
        self.Play = Button(self)
        self.Play['text'] = 'Play'
        self.Play['command'] = self.PlayPlay
        self.Play.place(x=30, y =270)

        ###### for testing background part
        # self.clef_photo = PhotoImage(file="3u7.gif")
        # self.aaa = PhotoImage(file="quarter.gif")
        # canvas.create_image(30, 30, image=self.clef_photo)
        # canvas.create_image(30, 70, image=self.aaa)

        ###### keyboard.gif on the canvas
        self.keyboard = PhotoImage(file='keyboard.gif')
        canvas.create_image(778, 688, image=self.keyboard)

        # right-hand dot
        # self.right = PhotoImage(file='right.gif')
        # canvas.create_image(784, 720, image=self.right)



    ###### open-file function
    def openfile(self):
        # open the window for choose the filename '*.mid' & '*.xml'
        root.fileName = filedialog.askopenfilename( filetypes = (("Musicxml","*.xml"),("midi file","*.mid")))
        print(root.fileName)

        # call the funtion : parsing_xml
        parsing_xml()
        print('in class')


    ###### button OK-funtion
    def OKOK(self):
        print('------------------------------------------------')
        print('OK button is click !')
        # self.create_image(0,0, image=self.clef_photo)

        print('daul is: ', self.var_daul.get())
        print('rhyt is: ', self.var_rhythm.get())

        print('mode is: ', self.box_mode.get())
        print('tona is: ', self.box_tona.get())

        print('temp is: ', self.scale.get())

    ###### button-Play funtion
    def PlayPlay(self):
        print('Play button is click !')

        print('Play button is click !')

    ###### menu-Exit funtion
    def client_exit(self):
        exit()
        
    # def MIDI_note(self):
    #     pygame.init()
    #     pygame.midi.init()   
        
    #     inp = pygame.midi.Input(1)
    #     print('start')
    #     while True:
    #         if (inp.poll()):
    #             print('in')
    #             note = inp.read(10)
    #             print (note)

def parsing_xml():
    print('in parsing')


''' 
# after 

def task():
    
    pygame.init()
    pygame.midi.init() 

    print("hello") 

    inp = pygame.midi.Input(1)
    print('inp: ', inp)
    print('poll: ', inp.poll())
    
    while True:
        if (inp.poll()):
            print('in')
            note = inp.read(10)
            print (note)
    
    root.after(1000, task)  # reschedule event in 1 seconds
''' 


if __name__ == '__main__':        

    root = Tk()
    root.geometry("500x400")
    # root.geometry("1300x700")

    app = Window(root)     

    # root.after(1000, task)
    root.mainloop()

