from tkinter import *
from tkinter import filedialog
from docutils.nodes import header
import cv2
import numpy as np
import imageio
from picture import windows


class Window:
    def __init__(self):
        self.win=Tk()
        self.win.configure(bg="#E0E0E0")
        self.win.geometry("650x350")
        self.win.title("myWindow")
        self.w=None
        self.bt1=Button(self.win,text="add picture",bg="#E00518",width=20,height=4)
        self.bt2 = Button(self.win, text="black and white",bg="#FF7F27",width=20,height=4 )
        self.bt3 = Button(self.win, text="cut",bg="#FFFD55",width=20,height=4)
        self.bt4 = Button(self.win, text="write text",bg="#A1FB8E",width=20,height=4)
        self.bt5 = Button(self.win, text="add shape",bg="#64DADB",width=20,height=4)
        self.bt6 = Button(self.win, text="save",bg="#001FD6",width=20,height=4)
        self.bt7 = Button(self.win, text="exit",bg="#B32ABF",width=20,height=4)

        self.position()
        self.events()
        self.win.mainloop()
    def position(self):
        self.bt1.grid(row=0,column=0,pady=10,padx=40,sticky="nsew")
        self.bt2.grid(row=0,column=1)
        self.bt3.grid(row=0,column=2)
        self.bt4.grid(row=1,column=0,pady=10,padx=40,sticky="nsew")
        self.bt5.grid(row=1,column=1)
        self.bt6.grid(row=1,column=2,pady=10,padx=20,sticky="nsew")
        self.bt7.grid(row=2,column=1,pady=10,padx=40,sticky="nsew")
    def events(self):
        self.bt1.bind("<Button-1>",self.choose)
        self.bt2.bind("<Button-1>",self.change_color)
        self.bt4.bind("<Button-1>",self.write)
        self.bt3.bind("<Button-1>",self.cut)
        self.bt5.bind("<Button-1>",self.add_shape)
        self.bt6.bind("<Button-1>", self.save)
        self.bt7.bind("<Button-1>", self.exit)

    def change_color(self,event):
        self.w.change_color1()

    def save(self, event):
        self.w.save()
    def choose(self,event):
        file_name = filedialog.askopenfilename()
        self.w=windows(file_name)

    def write(self,event):
        self.w.write1()

    def cut(self,event):
        self.w.cut1()

    def add_shape(self,event):
        self.w.add_shape1()

    def exit(self,event):
        self.win.destroy()

w=Window()