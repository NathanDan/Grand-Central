#GRAND CENTRAL START UP
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
from PIL import Image, ImageTk

import time
import os
import sys
import pyglet

def Close(Window):
    time.sleep(4)#WAITS 4 SECONDS BEFORE CLOSING THE BACKGROUND/WINDOW
    Window.destroy()#THIS WILL CLOSE THE BACKGROUND/WINDOW AFTER THE LOGIN APPLICATION HAS LAUNCHED 
   
Window = Tk()#DEFING 'Window' AS THE ROOT OF THE PROGRAM 

IMG = PhotoImage(file="C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\STARTUP.png")#THIS IS THE PATH FOR TEH BACKGROUND OF THE STARTUP, LIKE WINDOWS AND MACOS 
l = Label (Window, image=IMG)#DEFING THE IMAGE AS THE BACKGROUND 
l.pack()#DISPLAYING THE IMAGE AS THE BACKGROUND

song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\MISC\\GC_START_UP.mp3')#THIS IS THE PATH FOR THE STARTUP SOUND OF GRAND CENTRAL 
song.play()#PLAYS THE STARTUP SOUND 

Window.overrideredirect(True)
Window.resizable(width=FALSE, height=FALSE)#MEANS THAT THE SIZE OF THE SCREEN CAN NOT BE ADJUST THE SCREEN SIZE 
Window.geometry("{0}x{1}+0+0".format(Window.winfo_screenwidth(), Window.winfo_screenheight()))#ADJUSTS THE SIZE OF THE STARTUP SCREEN TO THE RESOLUTION OF YOUR MONITOR 
Window.configure(background='White')#MAKES SURE THE WINDOW BEHIND THE BACKGROUND IS WHITE 

def LOGIN():
    
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\TK_LOGIN_v3.py") #THE PATH OF THE LOGIN APPLICATION
    Window.after(4000,Close(Window)) #ALLOWS FOR THE LOGIN APPLICATION TO LAUNCH AND THEN CLOSES THE WINDOW IN THE BACKGROUND

Window.after(4000,LOGIN) #ALLOWS FOR THE STARTUP SOUND TO PLAY AND THEN WILL LAUNCH THE LOGIN APPLICATION 
mainloop()


