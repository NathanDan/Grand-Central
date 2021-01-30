#Nathan Jones
#GRAND CENTRAL v3 - GFDM TEACH EDITION
#2018

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

#global variables - GREENFLY
correct=False
Glo_Juv=2
Glo_Adu=8
Glo_Sen=4
Glo_OLDjuv=2
GEN0=False
Glo_SENILEsuvRate=0.5
Glo_ADULTsuvRate=0.5
Glo_JUVENILEsuvRate=0.5
Glo_BirthRate=2
Glo_Gen0No=10
DATA=[]

def GREENFLY():

    print("""
    
     ██████╗ ██████╗ ███████╗███████╗███╗   ██╗███████╗██╗  ██╗   ██╗            
    ██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║██╔════╝██║  ╚██╗ ██╔╝            
    ██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║█████╗  ██║   ╚████╔╝             
    ██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║██╔══╝  ██║    ╚██╔╝              
    ╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║██║     ███████╗██║               
     ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝     ╚══════╝╚═╝               
                                                                                 
██████╗  █████╗ ████████╗ █████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗     
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║     
██║  ██║███████║   ██║   ███████║    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║     
██║  ██║██╔══██║   ██║   ██╔══██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║     
██████╔╝██║  ██║   ██║   ██║  ██║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
""")
    Funct_MENU()

def Funct_MENU():

    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("####################################")
    print("#       Welcome to the MENU        #")
    print("#                                  #")
    print("# ?. HELP                          #")
    print("#                                  #")
    print("# 1. SET Generation 0 Numbers      #")
    print("# 2. DISPLAY Generation 0 Numbers  #")
    print("# 3. RUN DATA MODEL                #")
    print("# 4. EXPORT DATA                   #")
    print("# 5. LOG OUT                       #")
    print("# 6. QUIT                          #")
    print("####################################")

    answer=input("What option do you choose? ")
    

    if answer == "1":
        print("LOADING...")
        Funct_GEN0SET()
        Funct_MENU()
        
    elif answer == "2":
        print("LOADING...")
        Funct_DISP0GEN()
        Funct_MENU()

    elif answer == "3":
        print("LOADING...")
        Funct_RUNATMO()
        Funct_MENU()

    elif answer == "4":
        print("LOADING...")
        Funct_SAVE()
        Funct_MENU()

    elif answer == "?":
        print("LOADING...")
        Funct_HELP()
        Funct_RETURN()

    elif answer == "5":
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\TK_LOGIN_v3.py")
        
    elif answer == "6":
        Scroll="\n"*70
        print(Scroll)
        print("GOOD BYE.....")
        time.sleep(5)
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-TEACH\\TK_TEACH_v3.py")

    else:
        print("ERROR! INVALID ENTRY! PLEASE TRY AGAIN ")
        Funct_MENU()

def Funct_ValueChanger(text,value,MiVal,MaVal):
    print(text)
    print("Min Value: "+str(MiVal))
    print("Max Value: "+str(MaVal))
    NEWvalue=input(" ")
    try:
        NEWvalue=float(NEWvalue)
    except:
        print("ERROR! Invalid Value!")
        NEWvalue=Funct_ValueChanger(text,value,MiVal,MaVal)
    if NEWvalue<MiVal or NEWvalue>MaVal:
        print("ERROR! Invalid Value!")
        print("Value must be within "+str(MiVal)+" and "+str(MiVal))
        NEWvalue=Funct_ValueChanger(text,value,MiVal,MaVal)

    return NEWvalue

def Funct_GEN0SET():
    global Glo_Juv
    global Glo_Adu 
    global Glo_Sen
    global Glo_SENILEsuvRate
    global Glo_ADULTsuvRate
    global Glo_JUVENILEsuvRate
    global Glo_BirthRate
    global Glo_Gen0No
    global GEN0

    Glo_Juv=Funct_ValueChanger("Enter the starting number of Juveniles",Glo_Juv,0,80)
    Glo_JUVENILEsuvRate=Funct_ValueChanger("Enter the survival rate of Juveniles", Glo_JUVENILEsuvRate,0,1) 

    Glo_Adu=Funct_ValueChanger ("Enter the starting number of Adult",Glo_Adu,0,80)
    Glo_ADULTsuvRate=Funct_ValueChanger ("Enter the survival rate of Adult", Glo_ADULTsuvRate,0,1) 

    Glo_Sen=Funct_ValueChanger ("Enter the starting number of Seniles",Glo_Sen,0,80)
    Glo_SENILEsuvRate=Funct_ValueChanger ("Enter the survival rate of Seniles", Glo_SENILEsuvRate,0,1)

    Glo_Gen0No=Funct_ValueChanger ("Enter the number of Generations",Glo_Gen0No,5,25)

    Glo_BirthRate=Funct_ValueChanger ("Enter Birth Rate",Glo_BirthRate,0,100)

    GEN0=True
    
    Funct_MENU()

def Funct_DISP0GEN():
    print("Generation 0")
    print("Juvenile's: "+str(Glo_Juv))
    print("Adult's: "+str(Glo_Adu))
    print("Senile's: "+str(Glo_Sen))

    Funct_MENU()

def Funct_RUNATMO():
    global GEN0
    
    if GEN0==True:
        Funct_RUN()
        Funct_MENU()

    else:
        print("NO GENERATION 0 VALUES SET!")
        Funct_MENU()

def Funct_RUN():
    global Glo_Juv
    global Glo_Adu
    global Glo_Sen
    global Glo_Gen0No
    global DATA
    global Glo_SENILEsuvRate
    global Glo_ADULTsuvRate
    global Glo_JUVENILEsuvRate
    global Glo_BirthRate
    global Glo_Gen0No
    global Glo_OLDjuv
    
    DATA=[]

    DATA.append(["GENERATION","JUVENILE","ADULT","SENILE","TOTAL"])

    Funct_DISPTable(0)

    for GENERATION in range(0,int (Glo_Gen0No+1)):
        DATA.append([str(round(GENERATION)),str(round(Glo_Juv)),str(round(Glo_Adu)),str(round(Glo_Sen)),str(round(Glo_Juv+Glo_Adu+Glo_Sen))])
        Funct_DISPTable(GENERATION+1)
        Glo_OLDjuv=Glo_Juv
        Glo_Sen=Glo_Sen*Glo_SENILEsuvRate
        Glo_Juv=Glo_Adu*Glo_BirthRate
        Glo_Adu=Glo_Adu*Glo_ADULTsuvRate
        Glo_Sen=Glo_Sen+Glo_Adu
        Glo_Adu=Glo_OLDjuv*Glo_JUVENILEsuvRate

    

def Funct_DISPTable(GEN):
    global DATA

    COL_WIDTH=12
    row=str(DATA[GEN][0])+" "* (COL_WIDTH-len(DATA[GEN][0]))
    row=row+str(DATA[GEN][1])+" "* (COL_WIDTH-len(DATA[GEN][1]))
    row=row+str(DATA[GEN][2])+" "* (COL_WIDTH-len(DATA[GEN][2]))
    row=row+str(DATA[GEN][3])+" "* (COL_WIDTH-len(DATA[GEN][3]))
    row=row+str(DATA[GEN][4])+" "* (COL_WIDTH-len(DATA[GEN][4]))
    print(row)

def Funct_CHECK(name):
    correct=True
    CHECK=name.split(".")
    if len(CHECK[0])>8:
        correct=False
    elif CHECK[1].upper()!=("CSV"):
        correct=False
    elif len(CHECK)!=2:
        correct=False
    else:
        for f in range (0,len(name)):
            sub_check=False
            if ord(name[f]) >96 and ord (name[f])<123:
                sub_check=True
            if ord(name[f]) >64 and ord(name[f])<91:
                sub_check=True
            if ord(name[f]) <46 and ord (name[f])>57:
                sub_check=True
            if ord(name[f])==46:
                sub_check=True
                
            if sub_check!=True:
                correct = False 
    return correct


def Funct_SAVE():
    global DATA
    global Glo_Gen0No

    print("For Example: C:Users" )
    pathway=input("Please enter file pathway: ")
    print(" ")
    print("This will be the pathway: "+str(pathway))
    print(" ")
    print("REMEMBER TO ADD '.CSV' ")
    print(" ")
    name=input("What is the name of the file: ")
    if Funct_CHECK(name):
        print(" ")
        print ("Filename and Pathway are CORRECT")
        print(" ")
    else:
        print(" ")
        print("Incorrect file name")
        print(" ")
        Funct_MENU() 
    completeName=os.path.join(pathway, name)
    file=open(completeName,"w")   

    for GEN in range(0,int(Glo_Gen0No+1)):
        row=str(DATA[GEN][0])+","
        row=row+str(DATA[GEN][1])+","
        row=row+str(DATA[GEN][2])+","
        row=row+str(DATA[GEN][3])+","
        row=row+str(DATA[GEN][4])+"\n"
        file.write(row)
    file.close()

def Funct_HELP():

    print("""
        Welcome to the HELP/INSTRUCTIONS for the data model!
        
This is the part that will tell you how to run the program, so let's begin:

First off you need to SET the Generation 0 numbers otherwise the program will not run.
To do this you need to select '1' on the main menu and follow the instructions,
when it comes to the survival rate you can select any number between 0 and 1.

After you have set the Generation o numbers you can then check them in the number '2'
option where the program will just print the numbers you selected and if you want to
change the numbers you can by selecting '1' back on the main menu.

Next you need to RUN the data model by selecting option '3' and the program will calculate
the data and display it in a table format.

Once you have RAN the data model you will then be able to save and EXPORT your data as a '.CSV'
in option '4' where you have to put a file pathway and file name where you have to add '.CSV' at
the end of the file name.

RECOMENDATION: WHEN SAVING CREATE A 'GREENFLY' FOLDER SOMEWHERE AND COPY THE ADDRESS AND
               INSERT IT IN THE FILE PATHWAY SECTION.
""")

def Funct_RETURN():
    
    answer=input("Would you like to return to main menu? Y/N: ")

    if answer == "Y":
        Scroll="\n"*70
        print(Scroll)
        Funct_MENU()   
        

    elif answer == "N":
        Funct_HELP()

    else:
        print("INVALID OPTION")
        Funct_RETURN()

GREENFLY()
