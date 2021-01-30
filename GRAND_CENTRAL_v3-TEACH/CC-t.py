#Nathan Jones
#GRAND CENTRAL v3 - CHATROOM CLIENT TEACH EDITION
#2018

#TEACHER'S CLIENT

from colorama import init
from colorama import Fore, Back, Style

import socket
import threading
import sys

init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

uname = Style.BRIGHT +Fore.GREEN + str("TEACHER") + Style.RESET_ALL 

ip = input('Enter the IP Address::')

s.connect((ip, port))
s.send(uname.encode('ascii'))

clientRunning = True

def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode('ascii')
            print(msg)
        except:
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
while clientRunning:
    tempMsg = input()
    msg = '<' + Style.BRIGHT +Fore.RED + str(uname) + Style.RESET_ALL + '> ' + tempMsg
    if '@quit' in msg:
        clientRunning = False
        s.send('@quit'.encode('ascii'))
    else:
        s.send(msg.encode('ascii'))
