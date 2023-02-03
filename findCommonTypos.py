#! python3 
#findCommonTypos.py     -> remove repeated,spaces,words ...

import re, pyperclip

text = pyperclip.paste()
text = text.lower()
repeatedWordRegex    = re.compile(r'(\b\w+\s?\w+?\b)(,|!)?\s\1')
repeatedSpacesRegex  = re.compile(r'\s{2,}')
repeatedExMarksRegex = re.compile(r'\!{2,}|\s\!')

# find the longest group 
def findLongest(): #getting the word that repeats too mush and take it as range len
    longest = []
    longest.append(repeatedWordRegex.findall(text,re.I))
    longest.append(repeatedSpacesRegex.findall(text,re.I))
    longest.append(repeatedExMarksRegex.findall(text,re.I))
    return len(max(longest,key=len))

print(findLongest()) #replace each word, !, and ' ' in repeated in the string with one on them
for i in range(findLongest()):
    text = re.sub(repeatedWordRegex,r'\1',text)
    text = re.sub(repeatedExMarksRegex,'!',text)
    text = re.sub(repeatedSpacesRegex,' ',text)
    
pyperclip.copy(text) 




# # -------------------exemple
# Wow Wow Wow !!! This is really exciting! Can you believe it?! This is amazing! Repeat, repeat,       repeat! Spaces, spaces, spaces! Exclamation marks, exclamation marks, exclamation marks So cool So exciting So amazing Wow Wow Wow !!!

# result

# wow! this is really exciting! can you believe it?! this is amazing! repeat! spaces! exclamation marks so cool so exciting so amazing wow!
