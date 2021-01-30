#Nathan Jones
#GRAND CENTRAL v3 - GFDM MSTR EDITION
#2018

from datetime import datetime #ALLOWING THE DATE AND TIME TO BE DISPLAYED

import time         #THIS ALLOWS FOR THE PROGRAM TO USE THE SLEEP FUNCTION WITHIN THE PROGRAM
import sys          #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON 
import os.path      #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THEGC MAIN MENU
import os           #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import string       #ALLOWS FOR DATA/ENTRIES TO BE RECOREDAS STRINGS AND NOT INDIVIDUAL CHARACTERS
import random       #THIS IMPORT ALLOWS FOR WORDS/LOCATIONS TO BE RANDOMLY SELECTED 
import statistics   #ALLOWS ACCESS TO THE STATISTICS LIBARY FOR THE DATA COLLECTION AND PROCESSING
import itertools    #ALLOWS ACCESS TO ACCESS TO THE ITERATORS LIBARY FOR EFFICENT LOOPING 
import datetime     #THIS ALLOWS FOR THE CURRENT TIME TO BE IMPORTED AND DISPLAYED FOR THE USER TO SEE 

correct=False       #SETTING THE CORRECT VALUE TO BE ITS DEFAULT STATE WHICH IN THIS CASE IS FALSE
Juv=2               #SETTING THE JUV VARIABLE DEFAULT VALUE 
Adu=8               #SETTING THE ADU VARIABLE DEFAULT VALUE
Sen=4               #SETTING THE SEN VARIABLE DEFAULT VALUE
OLDjuv=2            #SETTING THE OLDJUV VARIABLE DEFAULT VALUE
GEN0=False          #SETTING THE GEN0 VAIRIABLE TO 0 WHEN THE PROGRAM STARTS 
SENILEsuvRate=0.5   #SETTING THE DEFAULT SENILE SURVIVAL RATE TO 0.5 
ADULTsuvRate=0.5    #SETTING THE DEFAULT ADULT SURVIVAL RATE TO 0.5
JUVENILEsuvRate=0.5 #SETTING THE DEFAULT JUVENILE SURVIVAL RATE TO 0.5
BirthRate=2         #SETTING THE DEFAULT BIRTH RATE TO 2
Gen0No=10           #SETTING THE DEFAULT GENERATION NUMBERS TO BE 10 ON THE FIRST ROUND     
DATA=[]             #CREATING AN EMPTY ARRAY TO STORE THE DATA IN 

Time = datetime.datetime.now() #ALLOWING THE PROGRAM TO HAVE DIRECT ACCESS WITH THE CURRENT DATE AND TIME

def Scroll():
    
        Scroll="\n"*70 #CREATING A VARIABLE WHEN CALLED UPON WILL PRINT 70 LINES OF NOTHING TO ACT AS A SPACE 
        print(Scroll)  #PRNTING THE SCROLL AND ITS 70 LINES

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
    MENU() #TAKING THE USER TO THE MENU OF THE DATA MODEL

def MENU():

    print(("SYSTEM TIME: ")+str(Time.strftime("%Y-%m-%d %H:%M"))) #DISPLAYING THE CURRENT TIME IN THE FORMAT OF Y-M-D H:M
    print(" ")                                          #CREATING A ONE LINE SPACE 
    print("####################################")       #CREATING A BORDER WITH THE USE OF '#' 
    print("#       Welcome to the MENU        #")       #DISPLAYING THE WELCOME MESSAGE
    print("#                                  #")       #CREATING A ONE LINE SPACE IN THE MENU
    print("# ?. HELP                          #")       #DISPLAYING THE OPTION THAT WILL TAKE YOU TO THE HELP MESSAGE
    print("#                                  #")       #CREATING A ONE LINE SPACE IN THE MENU
    print("# 1. SET Generation 0 Numbers      #")       #DISPLAYING THE OPTION TO SET THE STARTING NUMBERS OF THE DATA SET 
    print("# 2. DISPLAY Generation 0 Numbers  #")       #DISPLAYING THE OPTION TO DISPLAY THE STARTING NUMBERS TO CHECK THEM 
    print("# 3. RUN DATA MODEL                #")       #DISPLAYING THE OPTION TO RUN THE ACTUAL DATA MODEL WITH THEIR NUMBERS
    print("# 4. EXPORT DATA                   #")       #DISPLAYING THE OPTION TO EXPORT THE DATA MODEL RESULTS TO A CSV FILE
    print("# 5. LOG OUT                       #")       #DISPLAYING THE OPTION TO ALLOWING THE USER TO LOG OUT FROM THE DATA MODEL
    print("# 6. QUIT                          #")       #DISPLAYING THE OPTION TO ALLOWING THE USER TO RETURN TO THEIR GRAND CNTRAL
    print("####################################")       #CREATING A BORDER WITH THE USE OF '#'

    answer=input("What option do you choose? ")         #DISPLAYING THE QUESTION TO THE USER SO THEY CAN INPUT THEIR CHOICE 
    
    if answer == "1":        #IF THEIR ANSWER IS 1 THE FOLLOWING WILL TAKE PLACE
        print("LOADING...")  #DISPLAYING A LOADING MESSAGE TO ACKNOWLEDGE THE SELECTION
        GEN0SET()            #TAKING THE USER TO THE FUNCTION THAT WILL ALLOW THEM TO SET THE GENERATION NUMBERS 
        MENU()               #TAKING THE USER BACK TO THE MENU AFTER THEY HAVE ENTERED THEIR VALUES  
        
    elif answer == "2":      #IF THEIR ANSWER IS 2 THE FOLLOWING WILL TAKE PLACE
        print("LOADING...")  #DISPLAYING A LOADING MESSAGE TO ACKNOWLEDGE THE SELECTION
        DISP0GEN()           #TAKING THE USER TO THE FUNCTION THAT WILL DISPLAY THEIR GENERATION 0 NUMBERS SO TAHT THEY CAN CHECK THEM 
        MENU()               #TAKING TEH USER BACK TO THE MENU AFTER TEHY HAVE CHECKED THEIR NUMBERS  

    elif answer == "3":      #IF THEIR ANSWER IS 3 THE FOLLOWING WILL TAKE PLACE 
        print("LOADING...")  #DISPLAYING A LOADING MESSAGE TO ACKNOWLEDGE THE SELECTION
        RUNATMO()            #TAKING TEH USER TO THE FUNCTION THAT WILL RUN THE DATA MODEL WITH THE NUMBERS ENTERED 
        MENU()               #TAKING TEH USER BACK TO THE MENU AFTER THE DATA MODEL HAS RUN  

    elif answer == "4":      #IF THEIR ANSWER IS 4 THE FOLLOWING WILL TAKE PLACE
        print("LOADING...")  #DISPLAYING A LOADING MESSAGE TO ACKNOWLEDGE THE SELECTION 
        SAVE()               #TAKING THE USER TO THE FUNCTION THAT WILL EXPORT THE DATA THAT HAS BEEN CREATED BY THE DATA MODEL
        MENU()               #TAKING THE USER BACK TO THE MENU AFTER THEY HAVE SAVED/EXPORTED THEIR DATA MODEL  

    elif answer == "?":      #IF THEIR ANSWER IS ? THE FOLLOWING WILL TAKE PLACE
        print("LOADING...")  #DISPLAYING A LOADING MESSAGE TO ACKNOWLEDGE THE SELECTION
        HELP()               #TAKING THE USER TO THE HELP FUNCTION WHICH WILL TELL THEM WHAT TO DO/USE THE PROGRAM   
        RETURN()             #TAKING THE USER TO A SEPERATE FUNCTION WHICH WILL ASK TEHM IF THEY WOULD LIKE TO GO BACK TO THE MENU 

    elif answer == "5":      #IF THEIR ANSWER IS 5 THE FOLLOWING WILL TAKE PLACE - TAKES THEM BACK TO THEIR GRAND CENTRAL 
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\TK_LOGIN_v3.py")
        
    elif answer == "6":        #IF THEIR ANSWER IS 6 THE FOLLOWING WILL TAKE PLACE
        Scroll()               #UTILISING THE SCROLL FUNCTION OF 70 EMPTY LINES
        print("GOOD BYE.....") #DISPLAYING A GOOD BYE MESSAGE TO ACKNOWLEDGE THE SELECTION
        time.sleep(5)          #MAKING THE PROGRAM WAIT 5 SECONDS BEFORE CARRYING OUT THE NEXT BIT - TAKING THE USER TO TEH GRAND CENTRAL LOG IN  
        os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-MSTR\\TK_MSTR_v3.py")

    else:                                                #IF ANYTHING ELSE IS INPUTTED THAN THOSE STATED ABOVE THE FOLLWING WILL HAPPEN 
        print("ERROR! INVALID ENTRY! PLEASE TRY AGAIN ") #DISPLAYING AN ERROR MESSAGE SO TAHT THE USER KNOWS WHAT HAS HAPPENED  
        MENU()                                           #TAKING TEH USER BACK TO THE MENU SO THEY CAN INPUT AN ANSWER AGAIN

def ValueChanger(text,value,MiVal,MaVal):  
    print(text)                            #DISPLAYING WHICH VARIABLE THEY ARE CHANGING                 
    print("Min Value: "+str(MiVal))        #DISPLAYING THE MINIMUM VALUE 
    print("Max Value: "+str(MaVal))        #DISPLAYING THE MAXIMUM VALUE 
    NEWvalue=input(" ")                    #THE NEW VALUE WILL BE WHATEVER THE USER ENTERS 
    try:
        NEWvalue=float(NEWvalue)           
    except:
        print("ERROR! Invalid Value!")                                #DISPLAYING AN ERROR MESSAGE STATING INVALID VALUE
        NEWvalue=ValueChanger(text,value,MiVal,MaVal)                 #THE NEW VALUE WILL NOW BE THE DEFAULT VALUES
    if NEWvalue<MiVal or NEWvalue>MaVal:                              #IF THE VALUE ENTERED IS HIGHER/LOWER THAN THE PARAMETERS THE FOLLOWING WILL HAPPEN 
        print("ERROR! Invalid Value!")                                #DISPLAYING AN ERROR MESSAGE STATING INVALID VALUE
        print("Value must be within "+str(MiVal)+" and "+str(MiVal))  #DISPLAYING A HELP MESSAGE SAYING WHAT THE VALUE HAS TO BE INBETWEEEN
        NEWvalue=ValueChanger(text,value,MiVal,MaVal)                 #THE NEW VALUE WILL NOW BE THE DEFAULT VALUES
    return NEWvalue                                                   #RETURNING THE NEW VALUE FOR THE DATA MODEL

def GEN0SET():
    global Juv             #GIVING THE FUNCTION ACCESS TO 'Juv' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Adu             #GIVING THE FUNCTION ACCESS TO 'Adu' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Sen             #GIVING THE FUNCTION ACCESS TO 'Sen' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global SENILEsuvRate   #GIVING THE FUNCTION ACCESS TO 'SENILEsuvRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global ADULTsuvRate    #GIVING THE FUNCTION ACCESS TO 'ADULTsuvRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global JUVENILEsuvRate #GIVING THE FUNCTION ACCESS TO 'JUVENILEsuvRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY 
    global BirthRate       #GIVING THE FUNCTION ACCESS TO 'BirthRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Gen0No          #GIVING THE FUNCTION ACCESS TO 'Gen0No' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global GEN0            #GIVING THE FUNCTION ACCESS TO 'GEN0' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY

    Juv=ValueChanger("Enter the starting number of Juveniles",Juv,0,80)                       #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES
    JUVENILEsuvRate=ValueChanger("Enter the survival rate of Juveniles", JUVENILEsuvRate,0,1) #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES 

    Adu=ValueChanger ("Enter the starting number of Adult",Adu,0,80)                          #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES
    ADULTsuvRate=ValueChanger ("Enter the survival rate of Adult", ADULTsuvRate,0,1)          #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES

    Sen=ValueChanger ("Enter the starting number of Seniles",Sen,0,80)                        #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES
    SENILEsuvRate=ValueChanger ("Enter the survival rate of Seniles", SENILEsuvRate,0,1)      #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES

    Gen0No=ValueChanger ("Enter the number of Generations",Gen0No,5,25)                       #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES
 
    BirthRate=ValueChanger ("Enter Birth Rate",BirthRate,0,100)                               #STATING WHAT VARIABLE THEY WILL BE CHANGING ALONG WITH THE MIN/MAX VALUES

    GEN0=True #SETTING THE GEN0 VARIABLE TO BE TRUE SO THE PROGRAM KNOWS THE USER HAS ENTERED THEIR GENERATION 0 VALUES 
    MENU()    #TAKING THE USER BACK TO THE MENU AUTOMATICALLY  

def DISP0GEN():
    print("Generation 0")           #DISPLAYING THE HEADER THAT STATES TAHT THE FOLLOWING VALUES ARE FOR GENERATION 0
    print("Juvenile's: "+str(Juv))  #DISPLAYING THE GENERATION 0 VALUES FOR JUVENILES 
    print("Adult's: "+str(Adu))     #DISPLAYING THE GENERATION 0 VALUES FOR THE ADULTS
    print("Senile's: "+str(Sen))    #DISPLAYING THE GENERATION 0 VALUES FOR THE SENILES
    MENU()                          #TAKING THE USER BACK TO THE MENU  

def RUNATMO():
    global GEN0     #GIVING THE FUNCTION ACCESS TO 'GEN0' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    
    if GEN0==True:  #IF THE GEN0 VARIABLE IS SET TO TRUE THE FOLLOWING WILL TAKE PLACE  
        RUN()       #TAKES THE USER TO THE FUNCTION THAT WILL RUN THE DATA MODEL
        MENU()      #TAKING THE USER BACK TO THE MENU AFTER THE DATA MODEL HAS RUN 

    else:           #IF THE GEN0 VARIABLE IS SET TO FALSE THE FOLLOWING WILL TAKE PLACE
            
        print("NO GENERATION 0 VALUES SET!") #DISPLAYING THE MESSAGE INFORMING THE USER THAT NO GENERATION 0 VALUES HAVE BEEN SET
        MENU()                               #TAKING THE USER BACK TO THE MENU

def RUN():
    global Juv             #GIVING THE FUNCTION ACCESS TO 'Juv' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Adu             #GIVING THE FUNCTION ACCESS TO 'Adu' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Sen             #GIVING THE FUNCTION ACCESS TO 'Sen' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Gen0No          #GIVING THE FUNCTION ACCESS TO 'Gen0No' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global DATA            #GIVING THE FUNCTION ACCESS TO 'DATA' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global SENILEsuvRate   #GIVING THE FUNCTION ACCESS TO 'SENILEsuvRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global ADULTsuvRate    #GIVING THE FUNCTION ACCESS TO 'ADULTsuvRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global JUVENILEsuvRate #GIVING THE FUNCTION ACCESS TO 'JUVENILEsuvRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global BirthRate       #GIVING THE FUNCTION ACCESS TO 'BirthRate' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Gen0No          #GIVING THE FUNCTION ACCESS TO 'Gen0No' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global OLDjuv          #GIVING THE FUNCTION ACCESS TO 'OLDjuv' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    
    DATA=[]                #CREATING THE EMPTY ARRAY TO HOUSE THE DATA FROM THE DATA MODEL

    DATA.append(["GENERATION","JUVENILE","ADULT","SENILE","TOTAL"]) #CREATING THE DIFFERENT TYPES OF DATA THAT WILL BE PRESENT

    DISPTable(0)           #STARTING THE DATA MODEL FORM GENERATION 0 

    for GENERATION in range(0,int (Gen0No+1)): #FOR EACH GENERATION THE FOLLOWING WILL TAKE PLACE 
        DATA.append([str(round(GENERATION)),str(round(Juv)),str(round(Adu)),str(round(Sen)),str(round(Juv+Adu+Sen))]) #APPENDING THE DATA TO THE MODEL
        DISPTable(GENERATION+1)    #DISPLAYING/DOING THE CALCULATIONS THE AMOUNT OF TIMES FOR THE GENERATIONS 
        OLDjuv=Juv                 #DEFINING THAT THE OLDjuv'S ARE EQUAL TO THE Juv'S
        Sen=Sen*SENILEsuvRate      #CREATING THE CALCULATIONS THAT WILL MAKE UP THE VARIABLE 
        Juv=Adu*BirthRate          #CREATING THE CALCULATIONS THAT WILL MAKE UP THE VARIABLE
        Adu=Adu*ADULTsuvRate       #CREATING THE CALCULATIONS THAT WILL MAKE UP THE VARIABLE
        Sen=Sen+Adu                #CREATING THE CALCULATIONS THAT WILL MAKE UP THE VARIABLE
        Adu=OLDjuv*JUVENILEsuvRate #CREATING THE CALCULATIONS THAT WILL MAKE UP THE VARIABLE

def DISPTable(GEN):
    global DATA  #GIVING THE FUNCTION ACCESS TO 'DATA' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY

    COL_WIDTH=12 #THE COLUMN WIDTH OF THE TABLE WILL BE 12
    row=str(DATA[GEN][0])+" "* (COL_WIDTH-len(DATA[GEN][0]))      #CREATING THE FIRST ROW OF DATA THAT WILL HOLD THE FIRST SET OF DATA
    row=row+str(DATA[GEN][1])+" "* (COL_WIDTH-len(DATA[GEN][1]))  #CREATING THE SECOND ROW OF DATA THAT WILL HOLD THE SECOND SET OF DATA 
    row=row+str(DATA[GEN][2])+" "* (COL_WIDTH-len(DATA[GEN][2]))  #CREATING THE THIRD ROW OF DATA THAT WILL HOLD THE THIRD SET OF DATA
    row=row+str(DATA[GEN][3])+" "* (COL_WIDTH-len(DATA[GEN][3]))  #CREATING THE FOURTH ROW OF DATA THAT WILL HOLD THE FOURTH SET OF DATA
    row=row+str(DATA[GEN][4])+" "* (COL_WIDTH-len(DATA[GEN][4]))  #CREATING THE FIFTH ROW OF DATA THAT WILL HOLD THE FIFTH SET OF DATA
    print(row)                                                    #DISPLAYING ALL OF THE ROWS IN ORDER FOR THE USER TO SEE 

def CHECK(name):
    correct=True                     #SETTING THE CORRECT VARIABLE TO BE TRUE 
    CHECK=name.split(".")            #CHECKING THAT THE NAME OF TEH FILE BY SPLITING THE FILENAME UP AT THE '.' PART
    if len(CHECK[0])>8:              #IF THE FILENAME IS LESS THAN 8 THE FOLLOWING HAPPENS 
        correct=False                #SETTING THE CORRECT VARIABLE TO BE FALSE
    elif CHECK[1].upper()!=("CSV"):  #CHECKING THAT THE FILENAME HAS .CSV AT THE END SO IT SAVE AS THE CORRECT TYPE OF FIRE 
        correct=False                #SETTING THE CORRECT VARIABLE TO BE FALSE
    elif len(CHECK)!=2:              #IF THE LENGTH IS NOT EQUAL TO 2 THE FOLLOWING HAPPENS      
        correct=False                #SETTING THE CORRECT VARIABLE TO BE FALSE
    else:                                              
        for f in range (0,len(name)):                  #THE SECTION UNDERNEATH IS CHECKING THE FILENAME USING ASCII VALUES AND IS CHECKING EACH SECTION   
            sub_check=False                            
            if ord(name[f]) >96 and ord (name[f])<123: 
                sub_check=True                         #SETTING THE SUB-CHECK VARIABLE TO BE TRUE                         
            if ord(name[f]) >64 and ord(name[f])<91:   
                sub_check=True                         #SETTING THE SUB-CHECK VARIABLE TO BE TRUE                        
            if ord(name[f]) <46 and ord (name[f])>57:  
                sub_check=True                         #SETTING THE SUB-CHECK VARIABLE TO BE TRUE    
            if ord(name[f])==46:                       
                sub_check=True                         #SETTING THE SUB-CHECK VARIABLE TO BE TRUE                                   

            if sub_check!=True:                        #IF THE SUB_CHECK VARIABLES ARE NOT TRUE THEN THE FOLLOWING WILL TAKE PLACE 
                correct = False                        #SETTING THE CORRECT VARIABLE TO BE FALSE                
    return correct

def SAVE():
    global DATA    #GIVING THE FUNCTION ACCESS TO 'DATA' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY
    global Gen0No  #GIVING THE FUNCTION ACCESS TO 'Gen0No' SO IT CAN UTILISE IT AND CHANGE IT IF NECCESSARY

    print("For Example: C:Users" )                   #DISPLAYING AN EXAMPLE DESTINATION WHEN SAVING THE DATA MODEL 
    pathway=input("Please enter file pathway: ")     #CREATING AN INPUT WHERE THE USER WILL INPUT THEIR FILE DESTINATION
    print(" ")                                       #CREATING A ONE LINE SPACE
    print("This will be the pathway: "+str(pathway)) #DISPLAYING THE PATHWAY THAT THE USER HAS JUST ENTERED
    print(" ")                                       #CREATING A ONE LINE SPACE
    print("REMEMBER TO ADD '.CSV' ")                 #DISPLAYING A NOTE TO REMIND THE USER TO ADD .CSV
    print(" ")                                       #CREATING A ONE LINE SPACE
    name=input("What is the name of the file: ")     #CREATING AN INPUT FOR THE USER TO ENTER THE FILENAME OF TEH DATA MODEL
    if Funct_CHECK(name):                            #AFTER THE FILENAME HAS BEEN CHECKED THE FOLLOWING WILL TAKE PALCE 
        print(" ")                                   #CREATING A ONE LINE SPACE 
        print ("Filename and Pathway are CORRECT")   #DISPLAYING A MESSAGE THAT LETS THE USER KNOW THAT WHAT THEY ENTERED WAS CORRECT
        print(" ")                                   #CREATING A ONE LINE SPACE
    else:                                            #IF THE FILENAME AND DESTININATION DID NOT CHECK OUT THEN THE FOLLOWING WILL TAKE PLACE 
        print(" ")                                   #CREATING A ONE LINE SPACE 
        print("Incorrect file name")                 #DISPLAYING AN ERROR MESSAGE SAYING THAT THE FILENAME IS INCORRECT  
        print(" ")                                   #CREATING A ONE LINE SPACE 
        MENU()                                       #TAKING THE USER BACK TO THE MENU 
    completeName=os.path.join(pathway, name)         #JOINING THE FILENAME AND DESTINATION TO CREATE THE FINAL DESTINATION 
    file=open(completeName,"w")                      #CREATING THE ACTUAL FILE TAHT WILL HOUSE THE DATA MODEL  

    for GEN in range(0,int(Glo_Gen0No+1)):           
        row=str(DATA[GEN][0])+","      #PUTTING THE DATA INTO THE FIRST ROW
        row=row+str(DATA[GEN][1])+","  #PUTTING THE DATA INTO THE SECOND ROW
        row=row+str(DATA[GEN][2])+","  #PUTTING THE DATA INTO THE THIRD ROW
        row=row+str(DATA[GEN][3])+","  #PUTTING THE DATA INTO THE FOURTH ROW
        row=row+str(DATA[GEN][4])+"\n" #PUTTING THE DATA INTO THE FIFTH ROW
        file.write(row)                #WRITING THE ROW FROM THE DATA ABOVE
    file.close()                       #CLOSING THE FILE ONCE IT HAS COMPLETED FOR ALL GENERATIONS

def HELP():

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
""")  #CREATING THE HELP MESSAGE THAT WILL BE DISPLAYED TO THE USER 

def RETURN():
    
    answer=input("Would you like to return to main menu? Y/N: ") #ASKING THE USER IF THEY WOULD LIKE TO RETURN BACK TO THE MENU 

    if answer == "Y":   #IF THE USER'S ANSWER IS Y THE FOLLOWING WILL TAKE PLACE
        Scroll()        #UTILISES TEH SCROLL FUNCTION AND LEAVES 70 BLANK LINES
        MENU()          #RETURNS THE USER BACK TO THE MENU
        
    elif answer == "N": #IF THE USER'S ANSWER IS N THE FOLLOWING WILL TAKE PLACE
        HELP()          #DISPLAYING THE HELP MENU AGAIN 

    else:                       #IF ANYTHING ELSE THE FOLLOWING WILL TAKE PLACE
        print("INVALID OPTION") #DISPLAYS AN INVALID MESSAGE SO THE USER KNOWS WHAT HAPPENED 
        RETURN()                #REPEATING THE QUESTION

GREENFLY()
