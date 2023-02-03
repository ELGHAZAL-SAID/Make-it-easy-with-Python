#! python3
#findUrls.py -> find urls that begins with http:// ans https:// in a clipboard then clean it and sort it 

import re, pyperclip

# urls finder Regex

urlsRegex = re.compile(
                        r'''
                        (http[s]?:\/\/[\w+\.]?\w+\.\w+)
                        '''
                        ,re.I|re.VERBOSE)


# url finder function 

def findUrls(text):
    matches = []
    answers = urlsRegex.findall(text) #getting regex groups in answers
    print(answers)
    for answer in answers:
        matches.append(answer) #stor each answer (group) in matches list 
    return matches

# getting the text from the clipboard
text = pyperclip.paste()

# ex of random text with random emails:
#     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse aliquam 
#     https://www.google.com velit vel suscipit facilisis. Integer posuere, http://www.example.com ipsum eu
#     viverra tincidunt, velit ante blandit elit, a mollis mi est at velit. Nam vel urna vel odio http://news.bbc.co.uk 
#     blandit euismod. Aliquam id varius eros. Integer https://www.reddit.com tempor lacus euismod semper facilisis. 
#     Proin id erat https://github.com sed magna rutrum congue. Sed eget nulla eget nibh convallis dictum. Nunc tempor dolor 
#     a massa hendrerit, a congue velit http://www.wikipedia.org faucibus. In euismod orci a metus commodo, at 
#     elementum https://stackoverflow.com velit tincidunt. Nulla facilisi. Sed http://www.apple.com vel aliquet odio. Aenean ac
#     magna quis https://www.amazon.com ipsum congue dapibus id a nibh. Morbi
#     at http://www.microsoft.com nisl nisi.

if len(findUrls(text)) > 0: #check if the return is greater than 0
    pyperclip.copy('\n'.join(findUrls(text))) #copying the returned list as a text to the clipboard
    print("\nFound URLs in clipboard:")
else:
    print("\nNo URLs found in clipboard.")


#-------------------result

# https://www.google
# http://www.example
# http://news.bbc
# https://www.reddit
# https://github.com
# http://www.wikipedia
# https://stackoverflow.com
# http://www.apple
# https://www.amazon
# http://www.microsoft