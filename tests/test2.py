#from tkinter import Tk, PhotoImage, Canvas
from tkinter import *
import tkinter.font as tkFont
 
class Interface(Tk):
    """ We're trying to clone login page of Windows 10 with Tkinter """
    def __init__(self, path_image):
        super(Interface, self).__init__()
 
        self.image = PhotoImage(file=path_image)
        self.w, self.h = self.image.width(), self.image.height()
 
        self.canvas = Canvas(self, width=self.w, height=self.h)
        self.canvas.pack()
        self.canvas.create_image((self.w//2, self.h//2), image=self.image)

        helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
        self.canvas.create_text((10, self.h-30), text="HugsBox 1.0", fill="white", font=helv36, anchor='w')
 
        self.mainloop()
 
         
 
Interface('insert_path_picture.gif')
