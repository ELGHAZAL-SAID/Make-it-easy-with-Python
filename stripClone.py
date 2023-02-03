#!python3
#stripClone.py => dose the same job strip method dose (remove whitespaces or passed character form the end of the word)

import re

def stripClone(text,x='\s'):

    pattern = r'(?:^[{x}]+)|(?:[{x}]+$)'.format(x=re.escape(x))

    text = re.sub(pattern,'',text)

    return text

print(stripClone('dddddddddTestdddddddddd','d'))


# output:
# Test