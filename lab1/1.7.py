try:
    while True:
        num=input()
        if num=='':
            break
        num = int(num)
        if num%8==2 or num%8==6:
            print("yes")
        else:
            print("no")
except EOFError:  
    pass 