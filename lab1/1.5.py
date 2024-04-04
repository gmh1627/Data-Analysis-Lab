n,m=map(int,input().split())
nums=[]
for i in range(m):
    num=list(map(int, input().split()))
    nums.append(num)
cost=0
sum=0
sorted_nums = sorted(nums, key=lambda x:x[0])
for i in range(m):
    if n-sum>sorted_nums[i][1]:
        cost+=sorted_nums[i][0]*sorted_nums[i][1]
        sum+=sorted_nums[i][1]
    else:
        cost+=sorted_nums[i][0]*(n-sum)
        break
print(cost)