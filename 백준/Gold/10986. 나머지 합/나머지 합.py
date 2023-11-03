import sys
N,M=map(int,sys.stdin.readline().split())
seq=list(map(int,sys.stdin.readline().split()))
parsumleft={}
temp=0
answer=0
for i in range(N):
    temp+=seq[i]
    x=temp % M
    if parsumleft.get(x):
        parsumleft[x]+=1
    else:
        parsumleft[x]=1
if parsumleft.get(0):
    answer=parsumleft[0]
for j in parsumleft.values():
    answer+=(j*(j-1)//2)
print(answer)