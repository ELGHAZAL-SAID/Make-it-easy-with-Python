#! python3 
#codeDetection.py -> for date detection and correction in DD/MM/YYYY

import re, pyperclip


text = pyperclip.paste()

pattern = r'''
            (\d{1,2}|\d{4})
            [/.-]
            (\d{1,2})
            [/.-]
            (\d{4}|\d{1,2})
            '''

matches = re.findall(pattern, text,flags=re.VERBOSE|re.I)

def getDate(matches):
    formatDate = []
    for match in matches:   
        dic = {}
        if len(list(match[0])) < 4 :
            day, month, year = match
        else :
            year, month,day = match
        dic['year']  = year
        dic['month'] = month.zfill(2)
        dic['day']   = day.zfill(2)
        formatDate.append(dic)
    return formatDate

def validDate(formatDate):
    valid_J_M_M_J_A_O_D = True 
    valid_N_A_J_S = True
    validFeb = True

    for date in formatDate:
        if int(date['month']) > 0 and int(date['day']) > 0 and int(date['year']) > 0:
            if int(date['year'])%4 == 0 and not int(date['year'])%100 == 0: 
                if date['month'] =='02':
                    if int(date['day']) > 29 :
                        validFeb = False
                    else:
                        validFeb = True
            else :
                if int(date['month']) == 2 and int(date['day']) > 28:
                    validFeb = False
                else:
                    validFeb = True
                    
            if int(date['month']) in [4, 6 ,9 ,11] :
                if int(date['month']) > 30:
                    valid_N_A_J_S = False
                else:
                    valid_N_A_J_S = True
            
            if int(date['month']) in [1,3,5,7,8,10,12]:
                if int(date['day']) > 31:
                    valid_J_M_M_J_A_O_D = False
                else:
                    valid_J_M_M_J_A_O_D = True
                
            if validFeb and valid_N_A_J_S and valid_J_M_M_J_A_O_D:
                date.setdefault('stats','valid')
            else:
                date.setdefault('stats','invalid')
        else:
            date.setdefault('stats','invalid')
    return formatDate


def printDates(dates):
    print('Date'.center(8)+'valid/invalid'.rjust(25))
    for date in dates:
        print(date["year"]+'/'+date['month']+'/'+date['day'].ljust(15),date['stats'].ljust(5))        

def toClipboard(dates):
    listOfDates = []
    for date in dates:
        listOfDates.append(date["year"]+'/'+date['month']+'/'+date['day']+' '+date['stats'])
    return listOfDates



if matches :
    pyperclip.copy('\n'.join(toClipboard(validDate(getDate(matches)))))
    print('Dates copied to the clipboard')
    printDates(validDate(getDate(matches)))
else:
    print('No dates fount in your clipboard. Please copy some text includes date format to your clipboard')


# ===========================test
# On 2000/02/28, John started his new job at ABC Company. He was very excited to be part of the team 28/02/2024 and was eager to prove himself. He 2000-02-29 had his first performance review on 33/12/2021 and was pleased to receive positive feedback from his manager. In early 2022, John was promoted to a senior role and his responsibilities increased significantly.


# result

# 2000/02/28 valid
# 2024/02/28 valid
# 2000/02/29 invalid
# 2021/12/33 invalid