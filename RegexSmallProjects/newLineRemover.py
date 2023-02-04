#! python3 
#newLineRemove.py => remove new lines from a given string from clipboard


import re , pyperclip

# niwLineRemover Regex

lineRegex = re.compile(r'\s+')

# get text from the clipboard
text = pyperclip.paste()

# replace every new line or tab or space+ with " "

answer = lineRegex.sub(' ',text)

# copy the restult the clipboard

pyperclip.copy(answer)