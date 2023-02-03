#!python3
#passwordValidation.py -> validating the password strength

import re

patternLen = r'\w{8,}'
patternNum = r'[1-9]+'
patternCase = r'[A-Z]'
patternSym  = r'[!@#$%^&*().,]+'


def validatePassword(password):
    input = password
    if re.search(patternLen, input) and re.search(patternNum, input) and re.search(patternCase,input) and re.search(patternSym,input):
        return True
    else:
        return False

if validatePassword('test'):
    print('strong enough')
else :
    print('not strong enough')

if validatePassword('testtesttest'):
    print('strong enough')
else:
    print('not strong enough')

if validatePassword('test13151485'):
    print('strong enough')
else:
    print('not strong enough')

if validatePassword('tesTT11515'):
    print('strong enough')
else :
    print('not strong enough')

if validatePassword('Test551578#@$'):
    print('strong enough')
else:
    print('not strong enough')