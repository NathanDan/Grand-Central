#Nathan Jones
#GRAND CENTRAL v3 - PC MSTR EDITION
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

def PIN():

    print(""" """)
    PIN_CRACK()

def PIN_CRACK():

    SCROLL2()
    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("####################################")
    print("#       Welcome to the MENU        #")
    print("#                                  #")
    print("#            ?. HELP               #")
    print("#                                  #")
    print("#            1. 4 PIN              #")
    print("#            2. 5 PIN              #")
    print("#            3. 6 PIN              #")
    print("#            4. 7 PIN              #")
    print("#            5. 8 PIN              #")
    print("#                                  #")
    print("#            Q. QUIT               #")
    print("#                                  #")
    print("####################################")

    answer=input("What option do you choose? ")

    if answer == "?":
       Scroll2="\n"*5
       SCROLL2()
       HELP()

    elif answer == "1":
       SCROLL()
       CRACK1()
       
    elif answer == "2":
       SCROLL()
       CRACK2()
       
    elif answer == "3":
       SCROLL()
       CRACK3()

    elif answer == "4":
       SCROLL()
       CRACK4()

    elif answer == "5":
       SCROLL()
       CRACK5()

    elif answer == "Q" or "q":
       SCROLL()
       print("GOODBYE!...")
       print(" ")
       print("LOADING...")
       time.sleep(5)
       SCROLL()
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")
       sys.exit()

    else:
       SCROLL()
       print(answer)
       print(" ")
       print("INVALID ANSWER! - TRY AGAIN")
       print(" ")
       PIN_CRACK()

def CRACK1():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 4 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 4)]
    print(a)
    SCROLL2()
    PIN_CRACK()
    
def CRACK2():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 5 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 5)]
    print(a)
    SCROLL2()
    PIN_CRACK()
    
def CRACK3():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 6 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 6)]
    print(a)
    SCROLL2()
    PIN_CRACK()

def CRACK4():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 7 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 7)]
    print(a)
    SCROLL2()
    PIN_CRACK()
    
def CRACK5():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 8 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 8)]
    print(a)
    SCROLL2()
    PIN_CRACK()

def CRACK1():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 4 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 4)]
    print(a)
    SCROLL2()
    PIN_CRACK()
    
def CRACK2():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 5 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 5)]
    print(a)
    SCROLL2()
    PIN_CRACK()
    
def CRACK3():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 6 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 6)]
    print(a)
    SCROLL2()
    PIN_CRACK()

def CRACK4():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 7 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 7)]
    print(a)
    SCROLL2()
    PIN_CRACK()
    
def CRACK5():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("*****************")
    n = input("ENTER 8 DIGITS:")
    print("*****************")
    print("LOADING...")
    SCROLL2()
    print("The Following Are The Possible Combinations: ")
    print(" ")
    a = [''.join(i) for i in itertools.permutations(n, 8)]
    print(a)
    SCROLL2()
    PIN_CRACK()

PIN()
