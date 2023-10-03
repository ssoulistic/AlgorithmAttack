import sys
n=int(sys.stdin.readline())
# n=int(input())
nums={}
nums_list=[]
for _ in range(n):
    m=int(sys.stdin.readline())
    # m=int(input())
    nums_list.append(m)
    if nums.get(m):
        nums[m]+=1
    else:
        nums[m]=1

many=0
for k,v in nums.items():
    if v>many:
        many=v
        many_n=[k]
    elif v==many:
        many_n.append(k)

    
print(int(round(sum(nums_list)/n,0)))
print(sorted(nums_list)[n//2])
if len(many_n)>=2:
    print(sorted(many_n)[1])
else:
    print(sorted(many_n)[0])
print(max(nums.keys())-min(nums.keys()))