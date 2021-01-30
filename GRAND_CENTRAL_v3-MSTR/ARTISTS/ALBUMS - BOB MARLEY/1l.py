#TKinter One Love
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

l0 = Label(window, text="",bg="old lace")
l0.pack()

#LOCATING THE ALBUM'S COVER/ARTWORK FOR THE PROGRAM TO THEN DISPLAY 
album = ImageTk.PhotoImage(Image.open("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\albums\\1l.jpg"))

#THIS LABEL IS DISPLAYING THE ALBUM'S COVER/ARTWORK FOR THE USER TO SEE
label = Label(window, image=album)
label.pack()

l2 = Label(window, text="",bg="old lace")
l2.pack()

#DISPLAYING THE ARTIST AND ALBUM NAME THAT HAS BEEN SELECTED
l2 = Label(window, text="Bob Marley & The Wailers - One Love", font='Helvetica 18 bold',bg="old lace")
l2.pack()

l1 = Label(window, text="",bg="old lace")
l1.pack()

#THIS LABEL GIVES A SMALL/BREIF SUMMARY OF THE ALBUM THAT HAS BEEN LOADED 
l1 = Label(window, text="""One Love: The Very Best of Bob Marley & The Wailers
is a compilation album of Bob Marley and the Wailers songs
that was released on the Island Records label in 2001.
""",bg="old lace")
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

l2 = Label(window, text="",bg="old lace")
l2.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option1():
    #1
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Stir It Up.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(219) #LENGTH OF THE SONG IN SECONDS
    option2() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                         Stir It Up                          ", command=option1) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option2():
    #2
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Get Up Stand Up.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(198) #LENGTH OF THE SONG IN SECONDS
    option3() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                  Get Up Stand Up                   ", command=option2) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option3():
    #3
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - I Shot The Sheriff.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(234) #LENGTH OF THE SONG IN SECONDS
    option4() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                   I Shot The Sheriff                 ", command=option3) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option4():
    #4
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Lively Up Yourself.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(311) #LENGTH OF THE SONG IN SECONDS
    option5() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
    

b1 = Button(window, text="                 Lively Up Yourself                  ", command=option4) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option5():
    #5
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - No Woman No Cry (Live).mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(429) #LENGTH OF THE SONG IN SECONDS
    option6() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()
  
b1 = Button(window, text="            No Woman No Cry (Live)          ", command=option5) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option6():
    #6
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Roots, Rock, Reggae.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(218) #LENGTH OF THE SONG IN SECONDS
    option7() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                Roots, Rock, Reggae               ", command=option6) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option7():
    #7
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Exodus.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(270) #LENGTH OF THE SONG IN SECONDS
    option8() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                           Exodus                           ", command=option7) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option8():
    #8
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Jamming.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(212) #LENGTH OF THE SONG IN SECONDS
    option9() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                         Jamming                         ", command=option8) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option9():
    #9
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Waiting In Vain.mp3')#DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(256) #LENGTH OF THE SONG IN SECONDS
    option10() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                    Waiting In Vain                    ", command=option9) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option10():
    #10
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Three Little Birds.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(180) #LENGTH OF THE SONG IN SECONDS
    option11() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                    Three Little Birds                 ", command=option10) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TOV
def option11():
    #11
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Turn Your Lights Down Low.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(219) #LENGTH OF THE SONG IN SECONDS
    option12() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="        Turn Your Lights Down Low         ", command=option11) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option12():
    #12
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - One Love.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(173) #LENGTH OF THE SONG IN SECONDS
    option13() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                        One Love                         ", command=option12) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option13():
    #13
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Is This Love.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(232) #LENGTH OF THE SONG IN SECONDS
    option14() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                        Is This Love                     ", command=option13) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option14():
    #14
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Sun Is Shining.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(298) #LENGTH OF THE SONG IN SECONDS
    option15() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                    Sun Is Shining                     ", command=option14) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option15():
    #15
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - So Much Trouble In The World.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(240) #LENGTH OF THE SONG IN SECONDS
    option16() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="     So Much Trouble In The World      ", command=option15) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option16():
    #16
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Could You Be Loved.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(237) #LENGTH OF THE SONG IN SECONDS
    option17() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="              Could You Be Loved               ", command=option16) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option17():
    #17
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Redemption Song (Band Version).mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(218) #LENGTH OF THE SONG IN SECONDS
    option18() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="   Redemption Song (Band Version)   ", command=option17) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option18():
    #18
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Buffalo Soldier.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(165) #LENGTH OF THE SONG IN SECONDS
    option19() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                   Buffalo Soldier                    ", command=option18) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option19():
    #19
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - Iron Zion Lion.mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(193) #LENGTH OF THE SONG IN SECONDS
    option20() #TAKES IT ONTO THE NEXT TRACK/FUNCTION
    pyglet.app.run()

b1 = Button(window, text="                   Iron Zion Lion                     ", command=option19) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack()

#CREATING A BUTTON FOR EACH SONG AS THE CLIENT/USER CAN CHOOSE WHICH SONG THEY WANT TO START LISTENING TO
def option20():
    #20
    song = pyglet.media.load('C:\\Users\\natda\\OneDrive\\Music\\Bob Marley\\One Love\\Bob Marley & The Wailers - I Know A Place (Single Rmx).mp3') #DEFINING WHERE THE SONG IS LOADED FROM
    song.play()
    time.sleep(225) #LENGTH OF THE SONG IN SECONDS
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\ALBUMS - BOB MARLEY\\1l.py") #REFRESHES THE CURRENT ALBUM PAGE AFTER ALL SONGS HAVE PLAYED 
    window.destroy()
    pyglet.app.run()

b1 = Button(window, text="       I Know A Place (Single Remix)     ", command=option20) #CREATING WHAT WILL BE DISPLAYED IN THE BUTTON
b1.pack() 

l2 = Label(window, text="",bg="old lace")
l2.pack()

#CREATING A BACK BUTTON SO THAT THE CLIENT/USER CAN RETURN BACK TO THE ALBUM PAGE 
def option14():
    os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\ARTISTS\\BM.py")
    window.destroy() #CLOSES THE CURRENT WINDOW THAT IS OPEN

b15 = Button(window, text="BACK",command=option14) #CREATING THE BACK BUTTON
b15.pack() #DISPLAYING THE BACK BUTTON

#DEFINING THE PROPERTIES AND CHARACTERISTICS OF THE WINDOW
window.resizable(0,0)
window.resizable(width=FALSE, height=FALSE) #MEANS THAT THE WINDOW SIZE CAN NOT BE CHANGED BY THE USER (NO FULL SCREEN)
window.title("One Love - MSTR") #GIVING A TITLE TO THE WINDOW 
window.geometry("500x940") #DEFING THE SIZE OF THE WINDOW - ALL ALBUM WINDOWS HAVE AN X-AXIS OF 500
window.configure(background="old lace") #DEFINING THE BACKGROUND COLOUR OF THE WINDOW 

mainloop()

