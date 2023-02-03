#! python3
#sensitiveInfoRemover.py -> remove sensitive info from a string

import re, pyperclip


text = pyperclip.paste()

# making Regex for each case we have.

sensitiveEmailRegex = re.compile(
                        r'''(
                        [a-z1-9-_.%]+   #email first part
                        @                #@ symbol
                        [a-z1-9_-]+     #domain name
                        (\.[a-z]{2,4})       #dot-something
                        )'''
                        ,re.VERBOSE|re.I|re.DOTALL)

sensitivePhoneRegex = re.compile(r'''(\b
                                    (\d{3}|\(\d{3}\))?  #first 3 digit number
                                    (\s|-|\.)?  #separator
                                    (\d{3}) #second 3 digits 
                                    (\s|-|\.)   #separator
                                    (\d{4}) #last 4 digits
                                    (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
                                    \b)''', re.VERBOSE|re.I|re.DOTALL)


sensitiveCreditCardRegex = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\s\d{3,4}\b', re.VERBOSE|re.I|re.DOTALL)

sensitiveBankAccountRegex = re.compile(r'([a-z]{2})?\d{5,30}', re.VERBOSE|re.I|re.DOTALL)

sensitivePasswordRegex = re.compile(r"password\s(for\s\w+\s)?(is)?\s[a-z1-9!@#$%^&*()-=\\/]{8,}", re.VERBOSE|re.I|re.DOTALL)


# replacing each case with a specific word

text = re.sub(sensitiveEmailRegex,'<EMAIL>',text)
text = re.sub(sensitivePhoneRegex,'<PHONE NUMBER>',text)
text = re.sub(sensitiveCreditCardRegex,'<CREDIT CARD NUMBER>',text)
text = re.sub(sensitiveBankAccountRegex,'<BANK ACCOUNT NUMBER>', text)
text = re.sub(sensitivePasswordRegex,'Password is <PASSWORD>',text)

pyperclip.copy(text)