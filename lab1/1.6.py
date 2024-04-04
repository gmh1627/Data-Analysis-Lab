n = int(input())  
nums = []  
for i in range(n):  
    nums.append(int(input()))
    
for i in nums:
    cnt=0
    m=i
    while m:
        if  m%10!=0 and i%(m%10)==0:
            cnt+=1
        m//=10#注意//才是整除
    print(cnt)