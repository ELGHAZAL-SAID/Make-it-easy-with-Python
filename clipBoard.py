#! python3
#clipBoard.py - A simple clipboard program.


#importing modules

import sys, pyperclip

EVERYDAYTOOLS = {
        'email': "username@domain.com",
        'phone': "+212 6 XXXXXXXX",
        'githubPass': "password here"
        }

# getting system commands : python fileName.py arg (email or phone or ...)
if len(sys.argv)<2: #checking if (python fileName.py) is followed by an arg
    print('Usage: python fileName.py [Keyphrase] (email ,phone ...) - to copy phrase text')
    exit()

# esle we store the key phrase from our list sys.argv (index 1 means the dictionary key we want to access)

keyphrase = sys.argv[1]   #first command line arg is the keyphrase

if keyphrase in TEXT.keys(): #check if the key phrase matches one of the dic keys above 
    pyperclip.copy(TEXT[keyphrase]) #the pyperclip.copy() used to copy the dic value to your clip board
    print('Text for '+keyphrase+' copied to clipboard')
else:
    print('There is no text fot '+keyphrase)
