m, n = map(int, input().split())
total=0
for i in range(m,n+1):
    if(i%2):
        total+=i
print(total)