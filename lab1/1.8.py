#使用正则表达式提取HTML代码中的歌手和歌名
import re

html=''
try:
    while True:
        line=input()
        html+=line
        if html.endswith('\n\n'):
            break
        #print(html)
except EOFError:  
    pass 
#print(html)

pattern=r'<a href=".*?" singer="([^"]+)">(.*?)</a>'
matches=re.finditer(pattern,html)
song_info=[(match.group(1),match.group(2)) for match in matches]
print(song_info)

    