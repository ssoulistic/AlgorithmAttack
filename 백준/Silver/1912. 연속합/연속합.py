T=int(input())
numbers=[0]+list(map(int,input().split()))
answer=[-1001]*(T+1)
for i in range(1,T+1):
    answer[i]=max(answer[i-1]+numbers[i],numbers[i])
print(max(answer))
