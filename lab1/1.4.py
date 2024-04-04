n=int(input())
nums=[]

for i in range(n):
    input_str=input()
    if input_str=='':
        break
    name, score_a, score_b = input_str.split()  
    score_a=int(score_a)
    score_b=int(score_b)
    num=[name,score_a,score_b]
    nums.append(num)
        

sorted_nums = sorted(nums, key=lambda x: (-x[1], -x[2], x[0]))#使用负数来实现降序排序 
  
for student in sorted_nums:  
    print(student[0],student[1],student[2])