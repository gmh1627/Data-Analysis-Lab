n = int(input())  
nums = []  
for i in range(n):  
    nums.append(int(input()))   
  
def isPrime(n):  
    if n == 2:  
        return True  
    for j in range(2, int(n**0.5) + 1):  
        if n % j == 0:  
            return False  
    return True  
  
def NearPrime(n):   
    for j in range(n-1, 1, -1):  
        if isPrime(j):  
            small = j  
            break  
    for j in range(n+1, 3*n): 
        if isPrime(j):  
            big = j  
            break  
    if (big - n) < (n - small):  
        return big  
    else:  
        return small 
    
for i in nums:  
    if isPrime(i):  
        print(i)  
    else: 
        print(NearPrime(i))  
        