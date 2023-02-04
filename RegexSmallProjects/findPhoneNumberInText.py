message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
phoneList = {}

for i in range(len(message)):
        check = message[i:i+12]
        if isPhoneNumber(check):
            print('Phone Number found:'+ check)
print('Done')