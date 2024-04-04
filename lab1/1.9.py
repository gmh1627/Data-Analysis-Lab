import re
text=''
try:
    while True:
        text+=input()
        if text.endswith('\n\n'):
            break
except EOFError:  
    pass

links=re.findall(r'http[s]?://[^"]*',text)
print(links)