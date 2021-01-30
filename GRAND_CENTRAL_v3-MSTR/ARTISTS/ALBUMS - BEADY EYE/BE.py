#TKinter Greatest Hits
#2018
#Nathan Jones

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from uuid import getnode as get_mac

import time
import socket
import sys
import os.path
import os
import string 
import getpass
import random
import statistics
import itertools
import datetime
import pyglet

window = Tk()

l0 = Label(window, text="",bg="antique white")
l0.pack()

#LOCATING THE ALBUM'S COVER/ARTWORK FOR THE PROGRAM TO THEN DISPLAY 
album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\BE.jpg"))

#THIS LABEL IS DISPLAYING THE ALBUM'S COVER/ARTWORK FOR THE USER TO SEE
label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="antique white")
l2.pack()

#DISPLAYING THE ARTIST AND ALBUM NAME THAT HAS BEEN SELECTED
l2 = Label(window, text="Beady Eye - BE", font='Helvetica 18 bold',bg="antique white")
l2.pack()

l1 = Label(window, text="",bg="antique white")
l1.pack()

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN LOADED 
l1 = Label(window, text="""BE is the second and final studio album by English rock band Beady Eye,
released on 10 June 2013. It was recorded between November 2012 and March 2013. 
BE debuted at number two on the UK Albums Chart behind Black Sabbath's 13.
""",bg="antique white")
l1.pack()

def donothing():
    pass

#CREATING THE 'PLAY ALL' BUTTON THAT WILL PLAY EACH TRACK STRATING FROM THE FIRST SONG IN THE ALBUM 
def option():

    option1()

b1 = Button(window, text="PLAY ALL", command=option)
b1.pack()

l2 = Label(window, text="",bg="antique white")
l2.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\01 - Flick of The Finger.mp3')
    song.play()
    time.sleep(226) #LENGTH OF THE SONG IN SECONDS
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                    Flick of The Finger                 ", command=option1)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\02 - Soul Love.mp3')
    song.play()
    time.sleep(310) #LENGTH OF THE SONG IN SECONDS
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="                           Soul Love                         ", command=option2)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\03 - Face The Crowd.mp3')
    song.play()
    time.sleep(240) #LENGTH OF THE SONG IN SECONDS
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="                     Face The Crowd                    ", command=option3)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\04 - Second Bite of The Apple.mp3')
    song.play()
    time.sleep(208) #LENGTH OF THE SONG IN SECONDS
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                 Second Bite of The Apple        ", command=option4)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\05 - Soon Come Tomorrow.mp3')
    song.play()
    time.sleep(298) #LENGTH OF THE SONG IN SECONDS
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="               Soon Come Tomorrow             ", command=option5)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\06 - Iz Rite.mp3')
    song.play()
    time.sleep(206) #LENGTH OF THE SONG IN SECONDS
    option7()
    pyglet.app.run()

b1 = Button(window, text="                             Iz Rite                             ", command=option6)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option7():
    #7
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\07 - I'm Just Saying.mp3")
    song.play()
    time.sleep(225) #LENGTH OF THE SONG IN SECONDS
    option8()
    pyglet.app.run()

b1 = Button(window, text="                    I'm Just Saying                      ", command=option7)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option8():
    #8
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\08 - Don't Brother Me.mp3")
    song.play()
    time.sleep(450) #LENGTH OF THE SONG IN SECONDS
    option9()
    pyglet.app.run()

b1 = Button(window, text="                   Don't Brother Me                  ", command=option8)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\09 - Shine A Light.mp3')
    song.play()
    time.sleep(304) #LENGTH OF THE SONG IN SECONDS
    option10()
    pyglet.app.run()

b1 = Button(window, text="                       Shine A Light                     ", command=option9)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\10 - Ballroom Figured.mp3')
    song.play()
    time.sleep(211) #LENGTH OF THE SONG IN SECONDS
    option11()
    pyglet.app.run()

b1 = Button(window, text="                    Ballroom Figured                 ", command=option10)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TOV
def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Beady Eye\\BE\\11 - Start Anew.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                        Start Anew                        ", command=option11)
b1.pack()

l2 = Label(window, text="",bg="antique white")
l2.pack()

#CREATING A BACK BUTTON SO THAT THE CLIENT/USER CAN RETURN BACK TO THE ALBUM PAGE 
def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\BeadyEye.py")
    window.destroy() #CLOSES THE CURRENT WINDOW THAT IS OPEN

b15 = Button(window, text="BACK",command=option14)
b15.pack()

#DEFINING THE PROPERTIES AND CHARACTERISTICS OF THE WINDOW
window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE) #MEANS THAT THE WINDOW SIZE CAN NOT BE CHANGED BY THE USER (NO FULL SCREEN)
window.title("BE - MSTR") #GIVING A TITLE TO THE WINDOW 
window.geometry("500x750") #DEFING THE SIZE OF THE WINDOW - ALL ALBUM WINDOWS HAVE AN X-AXIS OF 500
window.configure(background='antique white') #DEFINING THE BACKGROUND COLOUR OF THE WINDOW 

mainloop()


