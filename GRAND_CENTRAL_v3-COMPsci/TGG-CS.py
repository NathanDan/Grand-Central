#Nathan Jones
#GRAND CENTRAL v3 - TGG MSTR EDITION
#July 2018

from datetime import datetime

import time
import sys
import os.path
import os
import string 
import random
import statistics
import itertools
import datetime

def SCROLL():

    Scroll="\n"*70
    print(Scroll)

def SCROLL2():

    Scroll2="\n"*10
    print(Scroll2)

def SCROLL3():

    Scroll3="\n"*28
    print(Scroll3)      

def TEST_GRADE_GEN():

    print("""
████████╗███████╗███████╗████████╗                                           
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝                                           
   ██║   █████╗  ███████╗   ██║                                              
   ██║   ██╔══╝  ╚════██║   ██║                                              
   ██║   ███████╗███████║   ██║                                              
   ╚═╝   ╚══════╝╚══════╝   ╚═╝                                              
                                                                             
 ██████╗ ██████╗  █████╗ ██████╗ ███████╗                                    
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝                                    
██║  ███╗██████╔╝███████║██║  ██║█████╗                                      
██║   ██║██╔══██╗██╔══██║██║  ██║██╔══╝                                      
╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗                                    
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝                                    
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")
    SCROLL2()
    GRADE_GEN()

def GRADE_GEN():

    RES=[]

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    F_NAME=input("ENTER FIRST NAME:           ")
    L_NAME=input("ENTER LAST NAME:             ")
    AGE=input("ENTER AGE:                    ")
    FORM=input("ENTER FORM:                 ")
    print(" ")

    x = 0
    print(" ")
    while (x == 0):
        DATA=input("TEST SCORE: ")
        RES.append(int(DATA))
        LOOP=input("Do You Have Another? Y/N ")
        if LOOP =="n".upper():
            print(RES)
            x = x+1
        elif LOOP =="y".upper():
            print(RES)
            x = 0

    print(" ")
    statistics.stdev(RES)
    print(("Standard Deviation: ")+str(statistics.stdev(RES)))
    statistics.mean(RES)
    print(("Mean of Results: ")+str(statistics.mean(RES)))
    

    if statistics.mean(RES) <= 25:
        GRADE=("D")
    
    elif statistics.mean(RES) <= 50:
        GRADE=("C")

    elif statistics.mean(RES) <= 60:
        GRADE=("B")
        
    elif statistics.mean(RES) >= 80:
        GRADE=("A")
    
    print(" ")
    print("SAVING...")
    r=open("TEST SCORE FOR "+str(L_NAME),"w")
    r.write(("FIRST NAME:           ")+F_NAME+("\n"))
    r.write(("LAST NAME:            ")+L_NAME+("\n"))
    r.write(("AGE:                  ")+AGE+("\n"))
    r.write(("FORM:                 ")+FORM+("\n"))
    r.write(("GRADE:                ")+GRADE+("\n"))
    r.close()
    print("SAVE COMPLETE!")
    NEXT_STAGE()

def NEXT_STAGE():

        print(" ")
        print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
        print(" ")
        answer = input("Would You Like To Enter Another Person? Y/N ")
        if answer == "Y":
            SCROLL()
            print("LOADING...")
            print(" ")
            GRADE_GEN()
            print(" ")
    

        if answer == "N":
            SCROLL()
            print("GOODBYE!...")
            print(" ")
            SCROLL()
            print("LOADING...")
            time.sleep(5)
            os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")
            sys.exit()

        else:
            SCROLL()
            NEXT_STAGE()

TEST_GRADE_GEN()
