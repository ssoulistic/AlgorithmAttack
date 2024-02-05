import sys
input=sys.stdin.readline
N=int(input())
store=list(map(int,input().split()))
answer=0
last=2
for s in store:
    if s==0 and last==2:
        last=0
        answer+=1
    elif s==1 and last==0:
        last=1
        answer+=1
    elif s==2 and last==1:
        last=2
        answer+=1
print(answer)