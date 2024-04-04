str=input()
new_str=''
for i in str:
    if(i.isupper()):
        new_str += i.lower()
    elif(i.islower()):
        new_str += i.upper()
    else:
        new_str += i
print(new_str)