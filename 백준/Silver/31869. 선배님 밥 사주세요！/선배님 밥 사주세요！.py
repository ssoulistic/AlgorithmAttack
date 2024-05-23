import sys
input=sys.stdin.readline

N=int(input())
senpai={}
promise=[]
for _ in range(N):
    S,W,D,P=input().split()
    promise.append([7*int(W)+int(D),S])
    senpai[S]=int(P)
for _ in range(N):
    S,M=input().split()
    senpai[S]=int(M)-senpai[S]
promise.sort()
answer=0
last=-1
count=0
for day,name in promise:
    if last+1==day and senpai[name]>=0:
        last+=1
        count+=1
    elif last==day:
        continue
    else:
        if senpai[name]>=0:
            last=day
            count=1
    answer=max(answer,count)
print(answer)