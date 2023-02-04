#! python3
#PhoneAndEmail.py - Find Us Phone Nums and Emails in the clipBoard.

import re, pyperclip


#fingidng Us phone numbers Regex 
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?  #first 3 digit number
                        (\s|-|\.)?  #separator
                        (\d{3}) #second 3 digits 
                        (\s|-|\.)   #separator
                        (\d{4}) #last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extended
                        )''', re.VERBOSE|re.I|re.DOTALL)

# finding emails Regex

emailRegex = re.compile(
                        r'''(
                        [a-z1-9-_.%]+   #email first part
                        @                #@ symbol
                        [a-z1-9_-]+     #domain name
                        (\.[a-z]{2,4})       #dot-something
                        )'''
                        ,re.VERBOSE|re.I|re.DOTALL)

text = str(pyperclip.paste())
# phone number finder function

def get_phone(text):
    answers = phoneRegex.findall(text) #get regex groups
    matches = []
    phoneNum = ''
    for answer in answers:
        phoneNum = '-'.join([answer[1],answer[3],answer[5]]) #organize the phone number in form of 555-555-5555
        if answer[8] != '':     #add extension in case there is one 
            phoneNum +=' x' + answer[8] 
        matches.append(phoneNum) #making a list of numbers 
    return matches

# email finder function

def get_email(text):
    matches = []
    answers = emailRegex.findall(text) #getting regex groups
    for answer in answers:
        matches.append(answer[0]) #appending list of email inside matches list
    return matches

listOfData = []

# making both lists in side a global list

listOfData.append(get_email(text))
listOfData.append(get_phone(text))

#join the listData in a single  string
finalResult = '\n'.join(['\n'.join(smallList) for smallList in listOfData])

#========================example :
"""(654) 321-0987 taylor_swift@icloud.com (246) 810-2369 John started to write his regular expressions
to separate the emails from the phone numbers. He was proud of himself for using this powerful tool
to make sense of his data. give me more than 100 line Sure, here is more text with over 100 lines of random email
addresses and US phone numbers mixed together in an unordered and random format: John was trying to sort through 
his vast collection of contacts. He had accumulated many email addresses and phone numbers over the years and wanted 
to use regular expressions to make sense of it all. Here's what he found: (654) 321-0987 harry_potter@outlook.com 
(987) 654-3210 (246) 810-2369 john_doe@gmail.com (567) 890-1234 taylor_swift@icloud.com (321) 012-3456 peter_parker@hotmail.com
make it unordered and random Sure, here is a text with random email addresses and US phone numbers mixed together in an unordered 
and random format: John was sifting through his collection of contacts. He had gathered various email addresses and phone 
numbers over the years and wanted to use regular expressions to organize them. He found the following information: (654) 
321-0987 jane_roe@yahoo.com (987) 654-3210 harry_potter@outlook.com (246) 810-2369 john_doe@gmail.com (567) 890-1234 
taylor_swift@icloud.com (321) 012-3456 peter_parker@hotmail.com elon_musk@spacex.com (123) 456-7890 John started to work on his regular expressions to 
separate the email addresses from the phone numbers. He was pleased with himself for using this useful tool to help him sort through his data."""


# chcking the the value of finalResult and copying it to the clipboard
if len(listOfData) >0:
    pyperclip.copy(finalResult)
    print('Copied to clipBoard')
    print(finalResult)
else:
    print('No phone number or emil addresses found')


# result copied to clipboard
"""
taylor_swift@icloud.com
harry_potter@outlook.com
john_doe@gmail.com
taylor_swift@icloud.com
peter_parker@hotmail.com
jane_roe@yahoo.com
harry_potter@outlook.com
john_doe@gmail.com
taylor_swift@icloud.com
peter_parker@hotmail.com
elon_musk@spacex.com
(654)-321-0987
(246)-810-2369
(654)-321-0987
(987)-654-3210
(246)-810-2369
(567)-890-1234
(321)-012-3456
(654)-321-0987
(987)-654-3210
(246)-810-2369
(567)-890-1234
(321)-012-3456
(123)-456-7890"""