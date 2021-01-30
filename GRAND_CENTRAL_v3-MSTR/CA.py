#Nathan Jones
#GRAND CENTRAL v3 - CA MSTR EDITION
#2018

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 
from datetime import datetime                                      #ALLOWING THE DATE AND TIME TO BE DISPLAYED 

import time        #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS 
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC. 
import string      #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS 
import getpass     #WHEN CHECKING THE PASSWORD/USERNAME ALLOWS FOR A FUNCTION TO DO NOTHING AND PASS IT ON
import random      #THIS IMPORT ALLOWS FOR WORDS TO BE RANDOMLY SELECTED 
import statistics  #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools   #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime    #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 
 
window = Tk()      #DEFINING WHAT THE FIRST TKINTER WINDOW WILL BE DEFINED AS

window.resizable (0,0)                             #THE WINDOW WILL NOT ENTER FULLSCREEN MODE 
window.resizable (width=FALSE, height=FALSE)       #THE USER CANNOT CHANGE THE SIZE OF THE MENU
window.title ("CARD AUTHENTICATOR")                #GIVING THE WINDOW ITS NAME THAT WILL BE DISPLAYED IN THE BAR
window.geometry("300x150")                         #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE            
window.configure(background='white')               #CONFIGURING THE BACKGROUND OF THE WINDOW TO BE WHITE

def AUTH():

  time = datetime.datetime.now() #ALLOWS GRAND CENTRAL TO GATHER THE CURRENT TIME 
   
  DIGITS = int(auth.get())       #GATHERING THE 16-DIGIT CREDIT CARD NUMBER FROM THE ENTRY BOX 

  if not LENcheck(DIGITS):                                                                      #IF THE CARD NUMBER'S DOES NOT EQUAL 16 THEN THE FOLLOWING WILL HAPPEN
    l0 = Label(window, text='NOT A 16-DIGIT NUMBER', fg="red", background="white")              #CREATING THE LABEL THAT WILL DISPLAY THE INVALID CARD IN RED
    l0.pack()                                                                                   #DISPLAYING THE INVALID CARD LABEL  
  else:                                                                                         #IF THE CARD'S NUMBER HAS 16 DIGITS THEN THE FOLLOWING WILL HAPPEN 
    if not valid(DIGITS):                                                                       #IF THE CARD NUMBER'S FINAL SUM DOES NOT EQUAL 0 THEN THE FOLLOWING WILL HAPPEN      
      l = Label(window, text='INVALID CREDIT CARD NUMBER', fg="red", background="white")        #CREATING THE LABEL THAT WILL DISPLAY THE INVALID CARD
      l.pack()                                                                                  #DISPLAYING THE INVALID CARD LABEL 
    else:                                                                                       #IF THE CARD NUMBER'S FINAL SUM DOES EQUAL 0 THEN THE FOLLOWING WILL HAPPEN
      l1 = Label(window, text="SYSTEM TIME: "+str(time.strftime("%H:%M ")), background="white") #CREATING A LABEL THAT WILL DISPLAY THE CURRENT SYSTEM TIME 
      l1.pack()                                                                                 #DISPLAYING THE CURRENT SYSTEM TIME LABEL
      l2 = Label(window, text='VALID CREDIT CARD NUMBER', fg="green", background="white")       #CREATING A LABEL THAT WILL DISPLAY A MESSAGE THAT WILL SAY IT IS A VALID CARD IN GREEN 
      l2.pack()                                                                                 #DISPLAYING THE VALID CARD LABEL 


def LENcheck(DIGITS):          #THIS FUNCTION WILL CHECK THE LENGTH OF THE DIGITS TO MAKE SURE THEY ARE EQUAL TO 16
  length = len(str((DIGITS)))  #DEFINING WHAT 'length' WILL BE AND IN THIS CASE IT IS THE DIGITS THAT HAVE BEEN ENTERED BY THE USER 
  if (length == 16):           #IF THE VALUE OF 'length' IS EQUAL TO 16 THEN THE FOLLOWING WILL TAKE PLACE  
    return True                #IT WILL RETURN THE VALUE OF TRUE SO THAT THE PROGRAM CAN THEN BEGIN THE CALCULATIONS 
  else:                        #IF THE VALUE OF 'length' IS NOT EQUAL TO 16 THEN THE FOLLOWING WILL TAKE PLACE 
    return False               #IT WILL RETURN THE VALUE OF FALSE SO THAT THE PROGRAM WILL NOT COMPLETE ANY CALCULATIONS, RATHER IT WILL DISPLAY THE NOT VALID MESSAGE

def valid(DIGITS):             #THIS IS THE FUNCTION THAT WILL COMPLETE THE CALCULATIONS TO SEE IF THE CARD NUMBER IS A VALID ONE 
  card = DIGITS                #TAKING THE DIGITS THE USER HAS ENTERED AND NOW ASSIGNING THE DIGITTS TO A NEW VARIABLE 
  Digits = list((str(card)))   #THE VARIABLE THAT WAS CREATED ABOVE IS NOW BEING ASSIGNED AS A LIST AND STRING OF NUMBERS IN ANOTHER VARIABLE
  oddSUM = 0                   #SETTING THE VALUE OF 'oddSUM' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
  evenSUM = 0                  #SETTING THE VALUE OF 'evenSUM' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
  EVENcount = 0                #SETTING THE VALUE OF 'EVENcount' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
  ODDcount = 0                 #SETTING THE VALUE OF 'ODDcount' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
  totalSUM = 0                 #SETTING THE VALUE OF 'totalSUM' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
  length = 0                   #SETTING THE VALUE OF 'length' TO 0 AND THIS IS RESETING THE VALUE FOR THE CALCULATION TO TAKE PLACE
  for i in Digits:             
    length += 1                #CHANGING THE 'length' VARIABLE TO CREATE A COUNT THAT WILL ADD ONE FOR EACH DIGIT - THIS WILL KEEP TRACK OF THE LENGTH OF THE CARD NUMBER    
  count = 0                    #BUT KEEPING THE COUNT AS 0 SO THAT THE PROGRAM CAN KEEP TRACK 
  if length == 16:             
    ODDcount = 15              #CHANGING THE 'ODDcount' TO REPRESENT NEW COUNT FOR THE ODD DIGITS
    EVENcount = 14             #CHANGING THE 'EVENcount' TO REPRESENT NEW COUNT FOR THE EVEN DIGITS
  if length == 15:             
    ODDcount = 13              #CHANGING THE 'ODDcount' TO REPRESENT NEW COUNT FOR THE ODD DIGITS
    EVENcount = 14             #CHANGING THE 'EVENcount' TO REPRESENT NEW COUNT FOR THE EVEN DIGITS 

  while (count <= length-2):   #WHILE THE 'count' VARIABLE IS LOWER OR EQUAL TO THE 'length' VARIABLE BUT MINUS 2 THEN THE FOLLOWING WILL TAKE PLACE

    evenSUM += int(Digits[EVENcount])  #TAKING THE 'evenSUM' AND ADDING IT TO THE DIGITS AND 'EVENcount' 
    EVENcount -= 2                     #UPDATING THE 'EVENcount'   
   
    prod = 2 * int(Digits[ODDcount])   #CREATING A VARIABLE THAT IS 2 TIMES THE DIGITS AND 'ODDcount'
    oddSUM += prod                     #UPDATING THE 'oddSUM' WITH THE 'prod' VARIABLE BY ADDING IT 
    ODDcount -= 2                      #UPDATING THE 'ODDcount' TO BE WHATEVER IT IS MINUS 2   
    count += 2                         #UPDATING THE 'count' TO BE WHATEVER IT IS PLUS 2

  totalSUM = oddSUM + evenSUM          #THE FINAL OR 'totalSUM' IS MADE UP OF ADDING THE 'oddSUM' AND 'evenSUM' TOGETHER TO CREATE THE FINAL SUM  

  if totalSUM % 10 == 0:               #IF THE FINAL SUM CAN BE DIVIDED BY 10 THEN THE FOLLOWING WILL TAKE PLACE  
    return True                        #RETURNING THE TRUE VALUE SO THAT THE PROGRAM CAN DISPLAY THE VALID CARD MESSAGE
  else:                                #IF THE FINAL SUM CANNOT BE DIVIDED BY 10 THEN THE FOLLOWING WILL TAKE PLACE 
    return False                       #RETURNING THE FALSE VALUE SO THAT THE PROGRAM CAN DISPLAY THE INVALID CARD MESSAGE        

L = Label (window, text=" ", background="white")                               #CREATING A LABEL THAT WILL ACT LIKE A ONE LINE SPACE
   
Auth = Label (window, text="ENTER 16 DIGIT CARD NUMBER:", background="white")  #CREATING THE HEADER FOR THE WINDOW SO USERS KNOW WHAT TO DO   
auth = Entry (window, background="light grey")                                 #CREATING THE ENTRY BOX FOR THE USER TO ENTER THEIR 16 DIGITS 

AUTH = Button (text="      AUTHENTICATE      ", fg="blue", command=AUTH)       #CREATING THE BUTTON THAT WILL ALLOW THE USER TO PRESS WHICH WILL START THE CALCULATIONS  
label = Label(window, text=" ", background="white")                            #CREATING A LABEL THAT WILL ACT LIKE A ONE LINE SPACE

L.pack()      #DISPLAYING THE LABEL THAT WILL ACT AS A ONE LINE SPACE
Auth.pack()   #DISPLAYING THE HEADER FOR THE WINDOW  
auth.pack()   #DISPLAYING THE ENTRY BOX FOR THE USER TO INTERACT WITH
AUTH.pack()   #DISPLAYING THE BUTTON FOR THE USER TO INTERACT WITH 
label.pack()  #DISPLAYING THE LABEL THAT WILL ACT AS A ONE LINE SPACE

window.mainloop()

