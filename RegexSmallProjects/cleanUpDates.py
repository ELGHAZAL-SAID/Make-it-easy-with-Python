#! python3
#cleanUpDates.py => clear up date in a single standard format.

import re, pyperclip


# Create a regex for reformat the date 

dateRegex = re.compile(r'''
                        (\d{1,2}|\d{4})
                        [./-]
                        (\d{1,2})
                        [./-]
                        (\d{4}|\d{1,2})
                        ''',re.I|re.VERBOSE)

# create function for reforming the given matches 

def formatDate(match):
    if len(list(match.groups())[0]) < 4 :
        day, mount, year = match.groups()
    else :
        year, mount,day = match.groups()
    formatDate = f'{year}/{mount.zfill(2)}/{day.zfill(2)}'
    return formatDate

# get the text from the clipboard
text = pyperclip.paste()


# ========================== ex
# YYYY-MM-DD (e.g. 2022-12-31)
# DD/MM/YYYY (e.g. 31/12/2022)
# MM/DD/YYYY (e.g. 12/31/2022)
# YYYY.MM.DD (e.g. 2022.12.31)
# DD.MM.YYYY (e.g. 31.12.2022)
# MM.DD.YYYY (e.g. 12.31.2022)

# replace the dates found in the  clipboard with the new ones
text = re.sub(dateRegex,formatDate,text)

pyperclip.copy(text)

# ---------------------------result
# YYYY-MM-DD (e.g. 2022/12/31)
# DD/MM/YYYY (e.g. 2022/12/31)
# MM/DD/YYYY (e.g. 2022/31/12)
# YYYY.MM.DD (e.g. 2022/12/31)
# DD.MM.YYYY (e.g. 2022/12/31)
# MM.DD.YYYY (e.g. 2022/31/12)

