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

l0 = Label(window, text="",bg="lightgoldenrod")
l0.pack()

#LOCATING THE ALBUM'S COVER/ARTWORK FOR THE PROGRAM TO THEN DISPLAY 
album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\albums - AR\\BFS.jpg"))

#THIS LABEL IS DISPLAYING THE ALBUM'S COVER/ARTWORK FOR THE USER TO SEE
label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="lightgoldenrod")
l2.pack()

#DISPLAYING THE ARTIST AND ALBUM NAME THAT HAS BEEN SELECTED
l2 = Label(window, text="Bowling For Soup - The Songs People Actually Liked", font='Helvetica 14 bold',bg="lightgoldenrod")
l2.pack()

l1 = Label(window, text="",bg="lightgoldenrod")
l1.pack()

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN LOADED 
l1 = Label(window, text="""Songs People Actually Liked – Volume 1 – The First 10 Years is a compilation
album by American rock band Bowling for Soup, released on January 27, 2015.
The compilation was completely fan-funded, as well as being released
on the band's own record label like their previous albums.

""",bg="lightgoldenrod")
l1.pack()

def donothing():
    pass

#CREATING THE 'PLAY ALL' BUTTON THAT WILL PLAY EACH TRACK STRATING FROM THE FIRST SONG IN THE ALBUM 
def option():

    option1()

b1 = Button(window, text="PLAY ALL", command=option)
b1.pack()

l2 = Label(window, text="",bg="lightgoldenrod")
l2.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Last Rock Show.mp3')
    song.play()
    time.sleep(226) #LENGTH OF THE SONG IN SECONDS
    option2()
    pyglet.app.run()
    

b1 = Button(window, text="                    Last Rock Show                 ", command=option1)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Suckerpunch.mp3')
    song.play()
    time.sleep(310) #LENGTH OF THE SONG IN SECONDS
    option3()
    pyglet.app.run()
    

b1 = Button(window, text="                      Suckerpunch                    ", command=option2)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Emily.mp3')
    song.play()
    time.sleep(240) #LENGTH OF THE SONG IN SECONDS
    option4()
    pyglet.app.run()
    

b1 = Button(window, text="                            Emily                           ", command=option3)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Girl All the Bad Guys Want.mp3')
    song.play()
    time.sleep(208) #LENGTH OF THE SONG IN SECONDS
    option5()
    pyglet.app.run()
    

b1 = Button(window, text="              Girl All the Bad Guys Want     ", command=option4)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - You and Me.mp3')
    song.play()
    time.sleep(298) #LENGTH OF THE SONG IN SECONDS
    option6()
    pyglet.app.run()
  
b1 = Button(window, text="                        You and Me                    ", command=option5)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - The Bitch Song.mp3')
    song.play()
    time.sleep(206) #LENGTH OF THE SONG IN SECONDS
    option7()
    pyglet.app.run()

b1 = Button(window, text="                   The Bitch Song                   ", command=option6)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option7():
    #7
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Scope.mp3')
    song.play()
    time.sleep(225) #LENGTH OF THE SONG IN SECONDS
    option8()
    pyglet.app.run()

b1 = Button(window, text="                           Scope                           ", command=option7)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - 2113.mp3')
    song.play()
    time.sleep(450) #LENGTH OF THE SONG IN SECONDS
    option9()
    pyglet.app.run()

b1 = Button(window, text="                            2113                             ", command=option8)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Punk Rock 101.mp3')
    song.play()
    time.sleep(304) #LENGTH OF THE SONG IN SECONDS
    option10()
    pyglet.app.run()

b1 = Button(window, text="                     Punk Rock 101                  ", command=option9)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Belgium.mp3')
    song.play()
    time.sleep(211) #LENGTH OF THE SONG IN SECONDS
    option11()
    pyglet.app.run()

b1 = Button(window, text="                          Belgium                        ", command=option10)
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TOV
def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Life After Lisa.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                     Life After Lisa                    ", command=option11)
b1.pack()

def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Cody.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                            Cody                           ", command=option12)
b1.pack()

def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Thirteen.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                          Thirteen                        ", command=option13)
b1.pack()

def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Dance With You.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                 Dance With You                   ", command=option14)
b1.pack()

def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - KoolAid.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                         KoolAid                          ", command=option15)
b1.pack()

def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Pictures He Drew.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                  Pictures He Drew                 ", command=option16)
b1.pack()

def option17():
    #17
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - Sandwich.mp3')
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="                        Sandwich                        ", command=option17)
b1.pack()

def option18():
    #18
    song = pyglet.media.load("C:\\Users\\natda\\OneDrive\\Music\\Bowling For Soup\\Songs That People Actually Liked\\Bowling for Soup - 20 Years (That's a Lot of Beers).mp3")
    song.play()
    time.sleep(269) #LENGTH OF THE SONG IN SECONDS
    option12()
    pyglet.app.run()

b1 = Button(window, text="      20 Years (That's a Lot of Beers)      ", command=option18)
b1.pack()


l2 = Label(window, text="",bg="lightgoldenrod")
l2.pack()

#CREATING A BACK BUTTON SO THAT THE CLIENT/USER CAN RETURN BACK TO THE ALBUM PAGE 
def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\GENRES\\ALTERNATIVErockMENU.py")
    window.destroy() #CLOSES THE CURRENT WINDOW THAT IS OPEN

b15 = Button(window, text="BACK",command=option14)
b15.pack()

#DEFINING THE PROPERTIES AND CHARACTERISTICS OF THE WINDOW
window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE) #MEANS THAT THE WINDOW SIZE CAN NOT BE CHANGED BY THE USER (NO FULL SCREEN)
window.title("BE - MSTR") #GIVING A TITLE TO THE WINDOW 
window.geometry("500x910") #DEFING THE SIZE OF THE WINDOW - ALL ALBUM WINDOWS HAVE AN X-AXIS OF 500
window.configure(background='lightgoldenrod') #DEFINING THE BACKGROUND COLOUR OF THE WINDOW 

mainloop()
