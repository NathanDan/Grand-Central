#HARDWARE MONITOR 
#Nathan Jones
#2018

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry,END, LEFT, BOTH #ALLOWING FOR TKINTER TO BE UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS 
from tkinter import *                                                           #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED FOR USE IN THE GUI
from datetime import datetime                                                   #ALLOWING THE DATE AND TIME TO BE DISPLAYED 
from uuid import getnode as get_mac                                             #ALLOWING FOR THE PROGRAM TO DIRECTLY ACCESS THE MAC ADDRESS OF THE CURRENT MACHINE

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND ITS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass     #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import random      #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
import socket      #ALLOWS FOR THE PROGRAM TO GATHER IP AND MAC ADDRESSES
import psutil      #ALLOWS THE PROGRAM TO THE PSUTIL LIBARY THAT ALLOWS DIRECT ACCESS TO VARIOUS SENSORS WITHIN THE MACHINE

window = Tk()      #DEFINING WHAT THE TKINTER WINDOW WILL BE DEFINED AS

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT IP ADDRESS 
s.connect(("8.8.8.8", 80))                           #CONNECTS TO THE IP ADDRESS AND ESTABLISHES THE CONNECTION

window.resizable (0,0)                        #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
window.resizable (width=FALSE, height=FALSE)  #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title ("Grand Central Management")     #GIVING THE LOGIN WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("950x550")                    #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')          #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE LIGHT GREY 

time = datetime.datetime.now()                #ALLOWING THE PROGRAM TO ACCESS THE CURRENT TIME AND DATE  

l0 = Label(window, text="GRAND CENTRAL MONITOR",font='Helvetica 16 bold' ,bg="white") #GIVING THE WINDOW A HEADER SO THE USER KNOWS WHAT APPLICATION THEY ARE ON
L0 = Label(window, text="SYSTEM TIME: "+str(time.strftime("%Y-%m-%d %H:%M")),bg="white")         #DISPLAYING THE ACTUAL CURRENT TIME THAT HAS BEEN GATHERED FROM ABOVE  
                                                                            
def secs2hours(secs):
     mm, ss = divmod(secs, 60)            #CONVERTING THE DEFAULT VALUE OF JUST SECONDS INTO MINUTES AND SECONDS
     hh, mm = divmod(mm, 60)              #CHANGING THE DEFAULT VALUE OF JUST SECONDS INTO HOURS AND MINUTES 
     return "%d:%02d:%02d" % (hh, mm, ss) #RETURNING THE VALUE THAT HAS JUST BEEN CALCULATED 
battery = psutil.sensors_battery()        #CREATING THE VARIABLE THAT WILL HOLD THE NEW FIGURES THAT WILL BE DISPLAYED   

s1 = Label(window, text=" ", background="white") #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE
s2 = Label(window, text=" ", background="white") #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE
s3 = Label(window, text=" ", background="white") #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE
s4 = Label(window, text=" ", background="white") #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE
s5 = Label(window, text=" ", background="white") #CREATING A LABEL THAT WILL ACT AS A ONE LINE SPACE

l = Label(window, text="CPU MONITOR",font='Helvetica 10 bold' ,bg="white")                                              #CREATING A MINI HEADER FOR THE SECTION 
L = Label(window, text="Number of CPU's:            "+ str(psutil.cpu_count()),font='Helvetica 8 ',bg="white")          #DISPLAYING THE NUMBER OF CPU'S (REAL AND LOGIC)
L11 = Label(window, text="CPU Stats :                      "+ str(psutil.cpu_stats()),font='Helvetica 8 ',bg="white")   #DISPLAYING STATISTICS ABOUT THE CPU
L111 = Label(window, text="CPU Frequency (Mhz):   "+ str(psutil.cpu_freq(percpu=False)),font='Helvetica 8 ',bg="white") #DISPLAYING CURRENT CPU FREQUENCIES

N1 = Label(window, text="NETWORK MONITOR",font='Helvetica 10 bold' ,bg="white")                                                                #CREATING A MINI HEADER FOR THE SECTION  
N11 = Label(window, text="Network Status:              " +str(psutil.net_io_counters(pernic=False, nowrap=True)),font='Helvetica 8 ',background="white")#DISPLAYING THE NETWORK STATUS
N111 = Label(window, text="Network IP Address:      " +str(s.getsockname()[0]),font='Helvetica 8 ',background="white")                                  #DISPLAYING THE IP ADDRESS
N1111 = Label(window, text="MAC Address:                " +str(get_mac()),font='Helvetica 8 ',background="white")                                       #DISPLAYING THE MAC ADDRESS

l2 = Label(window, text="MEMORY MONITOR",font='Helvetica 10 bold' ,bg="white")                                                     #CREATING A MINI HEADER FOR THE SECTION 
L2 = Label(window, text="Current Memory Usage (Bytes):    " +str(psutil.virtual_memory()),font='Helvetica 8 ', background="white") #DISPLAYING MEMORY USAGE
L3 = Label(window, text="Swapped Memory (Bytes):            " +str(psutil.swap_memory()),font='Helvetica 8 ', background="white")  #DISPLAYING SWAPPED MEMORY

l6 = Label(window, text="DISK MONITOR",font='Helvetica 10 bold' ,bg="white")                                                       #CREATING A MINI HEADER FOR THE SECTION   
L6 = Label(window, text="Disk Usage (Bytes):              " +str(psutil.disk_usage('/')),font='Helvetica 8 ', background="white")  #DISPLAYING DISK USAGE 
L66 = Label(window, text="Disk IO Counters (Bytes):      " +str(psutil.disk_io_counters(perdisk=False,nowrap=True)),font='Helvetica 8 ', background="white")#DISPLAYING THE IO COUNTERS

l4 = Label(window, text="SYSTEM INFORMATION",font='Helvetica 10 bold' ,bg="white")    #CREATING A MINI HEADER FOR THE SECTION THAT WILL DISPLAY THE SYSTEM RUNNING TIME 
L4 = Label(window, text="System Running Since:     " +str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")),font='Helvetica 8 ', background="white")

l5 = Label(window, text="BATTERY INFORMATION",font='Helvetica 10 bold' ,bg="white")   #CREATING A MINI HEADER FOR THE SECTION FOR THE SECTION THAT WILL DISPLAY THE BATTERY INFORMATION
L5 = Label(window, text="Battery Status:                  " +str("Charge = %s%%, Time Left = %s" % (battery.percent, secs2hours(battery.secsleft))),font='Helvetica 8 ', background="white")

l0.pack()            #DISPLAYS THE ACTUAL HEADER OF THE WINDOW AT THE TOP OF THE WINDOW
L0.pack()            #DISPLAYS THE ACTUAL CURRENT TIME AT THE TOP OF THE WINDOW
 
l.pack(anchor=NW)    #DISPLAYS THE ACTUAL MINI HEADER FOR THE CPU INFORMATION
L.pack(anchor=NW)    #DISPLAYS THE ACTUAL THE NUMBER OF CPU'S (REAL AND LOGIC) ON THE LEFT HAND SIDE
L11.pack(anchor=NW)  #DISPLAYS THE ACTUAL CURRENT STATISTICS ABOUT THE CPU
L111.pack(anchor=NW) #DISPLAYS THE ACTUAL CURRENT CPU FREQUENCIES

s1.pack()            #DISPLAYS THE ONE LINE SPACE
N1.pack(anchor=NW)   #DISPLAYS THE ACTUAL MINI HEADER FOR THE NETWORK STATUS SECTION
N11.pack(anchor=NW)  #DISPLAYS THE ACTUAL CURRENT NETWORK STATUS
N111.pack(anchor=NW) #DISPLAYS THE ACTUAL IP ADDRESS
N1111.pack(anchor=NW)#DISPLAYS THE ACTUAL MAC ADDRESS

s2.pack()            #DISPLAYS THE ONE LINE SPACE
l2.pack(anchor=NW)   #DISPLAYS THE ACTUAL MINI HEADER FOR THE MEMORY SECTION
L2.pack(anchor=NW)   #DISPLAYS THE ACTUAL CURRENT MEMORY USAGE
L3.pack(anchor=NW)   #DISPLAYS THE ACTUAL CURRENT SWAPPED MEMORY

s3.pack()            #DISPLAYS THE ONE LINE SPACE
l6.pack(anchor=NW)   #DISPLAYS THE ACTUAL MINI HEADER FOR THE DISK MONITOR SECTION
L6.pack(anchor=NW)   #DISPLAYS THE ACTUAL CURRENT DISK USAGE
L66.pack(anchor=NW)  #DISPLAYS THE ACTUAL IO COUNTERS 

s4.pack()            #DISPLAYS THE ONE LINE SPACE
l4.pack(anchor=NW)   #DISPLAYS THE ACTUAL MINI HEADER FOR THE SYSTEM INFORMATION SECTION
L4.pack(anchor=NW)   #DISPLAYS THE ACTUAL CURRENT SYSTEM INFORMATION

s5.pack()            #DISPLAYS THE ONE LINE SPACE
l5.pack(anchor=NW)   #DISPLAYS THE ACTUAL MINI HEADER FOR THE BATTERY STATUS SECTION
L5.pack(anchor=NW)   #DISPLAYS THE ACTUAL CURRENT BATTERY STATUS 

window.mainloop()    
