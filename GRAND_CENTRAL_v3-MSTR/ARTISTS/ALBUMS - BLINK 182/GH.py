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

l0 = Label(window, text="",bg="lightgrey")
l0.pack()

#LOCATING THE ALBUM'S COVER/ARTWORK FOR THE PROGRAM TO THEN DISPLAY 
album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\GH.jpg"))

#THIS LABEL IS DISPLAYING THE ALBUM'S COVER/ARTWORK FOR THE USER TO SEE
label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="lightgrey")
l2.pack()

#DISPLAYING THE ARTIST AND ALBUM NAME THAT HAS BEEN SELECTED
l2 = Label(window, text="Blink 182 - Greatest Hits", font='Helvetica 18 bold',bg="lightgrey")
l2.pack()

l1 = Label(window, text="",bg="lightgrey")
l1.pack()

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN LOADED 
l1 = Label(window, text="""Greatest Hits is the first greatest hits album of American rock band Blink-182.
It was released on October 31, 2005 by Geffen Records.
Greatest Hits was created by Geffen shortly after the band's February 2005 breakup,
termed an "indefinite hiatus" by the label.
""",bg="lightgrey")
l1.pack()

def donothing():
    pass

def close_window (root): 
    root.destroy()

#CREATING THE 'PLAY ALL' BUTTON THAT WILL PLAY EACH TRACK STRATING FROM THE FIRST SONG IN THE ALBUM 
def option():

    option1()

b1 = Button(window, text="PLAY ALL", command=option)
b1.pack()

l2 = Label(window, text="",bg="lightgrey")
l2.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Carousel.mp3')
    song.play()
    time.sleep(191) #LENGTH OF THE SONG IN SECONDS
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                         Carousel                          ", command=option1)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option2():
    #2
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - M+M's.mp3''')
    song.play()
    time.sleep(155) #LENGTH OF THE SONG IN SECONDS
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="                           M+M's                           ", command=option2)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Dammit.mp3')
    song.play()
    time.sleep(165) #LENGTH OF THE SONG IN SECONDS
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="                         Dammit                           ", command=option3)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Josie (Radio Edit).mp3')
    song.play()
    time.sleep(185) #LENGTH OF THE SONG IN SECONDS
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="                 Josie (Radio Edit)                   ", command=option4)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option5():
    #5
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - What's My Age Again_.mp3''')
    song.play()
    time.sleep(148) #LENGTH OF THE SONG IN SECONDS
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="              What's My Age Again              ", command=option5)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - All the Small Things.mp3')
    song.play()
    time.sleep(171) #LENGTH OF THE SONG IN SECONDS
    option7()
    pyglet.app.run()

b1 = Button(window, text="                All The Small Things              ", command=option6)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option7():
    #7
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Adam's Song.mp3''')
    song.play()
    time.sleep(246) #LENGTH OF THE SONG IN SECONDS
    option8()
    pyglet.app.run()

b1 = Button(window, text="                     Adam's Song                      ", command=option7)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Man Overboard.mp3')
    song.play()
    time.sleep(167) #LENGTH OF THE SONG IN SECONDS
    option9()
    pyglet.app.run()

b1 = Button(window, text="                   Man Over Board                   ", command=option8)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - The Rock Show.mp3')
    song.play()
    time.sleep(168) #LENGTH OF THE SONG IN SECONDS
    option10()
    pyglet.app.run()

b1 = Button(window, text="                     The Rock Show                  ", command=option9)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - First Date.mp3')
    song.play()
    time.sleep(170) #LENGTH OF THE SONG IN SECONDS
    option11()
    pyglet.app.run()

b1 = Button(window, text="                           First Date                       ", command=option10)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TOV
def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Stay Together for the Kids.mp3')
    song.play()
    time.sleep(232) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="         Stay Together For The Kids          ", command=option11)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Feeling This.mp3')
    song.play()
    time.sleep(173) #LENGTH OF THE SONG IN SECONDS
    option13()
    pyglet.app.run()

b1 = Button(window, text="                        Felling This                      ", command=option12)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - I Miss You.mp3')
    song.play()
    time.sleep(227) #LENGTH OF THE SONG IN SECONDS
    option14()
    pyglet.app.run()

b1 = Button(window, text="                          I Miss You                      ", command=option13)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Down (Single Version).mp3')
    song.play()
    time.sleep(192) #LENGTH OF THE SONG IN SECONDS
    option15()
    pyglet.app.run()

b1 = Button(window, text="             Down (Single Version)              ", command=option14)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Always.mp3')
    song.play()
    time.sleep(257) #LENGTH OF THE SONG IN SECONDS
    option16()
    pyglet.app.run()

b1 = Button(window, text="                           Always                          ", command=option15)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Not Now.mp3')
    song.play()
    time.sleep(263) #LENGTH OF THE SONG IN SECONDS
    option17()
    pyglet.app.run()

b1 = Button(window, text="                         Not Now                        ", command=option16)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option17():
    #17
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Another Girl Another Planet.mp3')
    song.play()
    time.sleep(161) #LENGTH OF THE SONG IN SECONDS
    option18()
    pyglet.app.run()

b1 = Button(window, text="        Another Girl Another Planet        ", command=option17)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option18():
    #18
    song = pyglet.media.load('''C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - I Won't Be Home for Christmas.mp3''')
    song.play()
    time.sleep(197) #LENGTH OF THE SONG IN SECONDS
    option19()
    pyglet.app.run()

b1 = Button(window, text="    I Won't Be Home For Christmas     ", command=option18)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option19():
    #19
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Blink 182\\Greatest Hits\\Blink-182 - Go (BBC Radio 1 Session).mp3')
    song.play()
    time.sleep(111) #LENGTH OF THE SONG IN SECONDS
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\GH.py") #REFRESHES THE CURRENT ALBUM PAGE AFTER ALL SONGS HAVE PLAYED 
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="           Go (BBC Radio 1 Session)          ", command=option19)
b1.pack() 

l2 = Label(window, text="",bg="lightgrey")
l2.pack()

#CREATING A BACK BUTTON SO THAT THE CLIENT/USER CAN RETURN BACK TO THE ALBUM PAGE 
def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\Blink182.py")
    window.destroy() #CLOSES THE CURRENT WINDOW THAT IS OPEN

b15 = Button(window, text="BACK",command=option14)
b15.pack()

#DEFINING THE PROPERTIES AND CHARACTERISTICS OF THE WINDOW
window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE) #MEANS THAT THE WINDOW SIZE CAN NOT BE CHANGED BY THE USER (NO FULL SCREEN)
window.title("Greatest Hits - MSTR") #GIVING A TITLE TO THE WINDOW 
window.geometry("500x940") #DEFING THE SIZE OF THE WINDOW - ALL ALBUM WINDOWS HAVE AN X-AXIS OF 500
window.configure(background='lightgrey') #DEFINING THE BACKGROUND COLOUR OF THE WINDOW 

mainloop()

