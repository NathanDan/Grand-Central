#Nathan Jones
#GRAND CENTRAL v3 - CA TEACH EDITION
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

def SCROLL():

    Scroll="\n"*70
    print(Scroll)

def SCROLL2():

    Scroll2="\n"*10
    print(Scroll2)

def SCROLL3():

    Scroll3="\n"*28
    print(Scroll3)      


def AUTH():

    print("""
 ██████╗ █████╗ ██████╗ ██████╗                                                                           
██╔════╝██╔══██╗██╔══██╗██╔══██╗                                                                          
██║     ███████║██████╔╝██║  ██║                                                                          
██║     ██╔══██║██╔══██╗██║  ██║                                                                          
╚██████╗██║  ██║██║  ██║██████╔╝                                                                          
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝                                                                           
                                                                                                          
 █████╗ ██╗   ██╗████████╗██╗  ██╗███████╗███╗   ██╗████████╗██╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██║  ██║██╔════╝████╗  ██║╚══██╔══╝██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║██║   ██║   ██║   ███████║█████╗  ██╔██╗ ██║   ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██╔══██║██║   ██║   ██║   ██╔══██║██╔══╝  ██║╚██╗██║   ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗██║ ╚████║   ██║   ██║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")
    CARD_AUTH()


def CARD_AUTH():

   
    SCROLL2()
    print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
    print(" ")
    print("####################################")
    print("#       Welcome to the MENU        #")
    print("#                                  #")
    print("#            ?. HELP               #")
    print("#                                  #")
    print("#        1. AUTHENTICATE           #")
    print("#        2. PIN CODE CRACK         #")
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
       AUTH()

    elif answer == "2":
       SCROLL()
       CRACK1()
       

    elif answer == "Q" or "q":
       SCROLL()
       print("GOODBYE!...")
       print(" ")
       print("LOADING...")
       time.sleep(5)
       SCROLL()
       os.startfile("C:\\Users\\natda\\OneDrive\\Sixth Form\\Computer Science\\CODE\GRAND CENTRAL v3\\GRAND_CENTRAL_v3-TEACH\\TK_TEACH_v3.py")
       sys.exit()

    else:
       SCROLL()
       print(answer)
       print(" ")
       print("INVALID ANSWER! - TRY AGAIN")
       print(" ")
       CARD_AUTH()



def len_check(x):
  length = len(str((x)))
  if (length == 15) or (length == 16):
    return True
  else:
    return False 

def is_valid(x):
  card = x
  num_list= list((str(card)))
  sum_odd = 0
  sum_even = 0
  even_count = 0
  odd_count = 0
  total_sum = 0
  length = 0
  for i in num_list:
    length += 1
  #print(length)
  count = 0
  if length == 16:
    odd_count = 15
    even_count = 14
  if length == 15:
    odd_count = 13
    even_count = 14
  #print(even_count)
  #print(odd_count)

  while (count <= length-2):

    #print('even count', even_count)
    #print('D-even', num_list[even_count])
    sum_even += int(num_list[even_count])
    even_count -=2
    #print('sum even', sum_even)

    #print('odd count', odd_count)
    #print('D-odd', num_list[odd_count])
    prod = 2 * int(num_list[odd_count])
    sum_odd += prod
    odd_count -=2
    #print('sum odd', sum_odd)

    count +=2

  total_sum = sum_odd + sum_even
  #print('total sum', total_sum)

  if total_sum % 10 == 0:
    return True
  else:
    return False



def AUTH():
  cc_num = int(input('Enter at 15 or 16-digit credit card number: '))

  if not len_check(cc_num):
    print('Not a 15 or 16-digit number')
    SCROLL2()
    AUTH()
  else:
    if not is_valid(cc_num):

      print(" ")  
      print('Invalid credit card number')
      SCROLL2()
      CARD_AUTH()
    else:
      print(" ")
      print(("SYSTEM TIME: ")+str(datetime.datetime.now()))
      print(" ")
      print('valid card number')
      SCROLL2()
      CRACK1()
      CARD_AUTH()

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
    CARD_AUTH()

AUTH()
