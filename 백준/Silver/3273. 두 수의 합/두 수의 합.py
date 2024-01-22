import sys
input=sys.stdin.readline
n=int(input())
seq=sorted(map(int,input().split()))
x=int(input())
answer=0
s=0
e=len(seq)-1
while s<e:
    if seq[s]+seq[e]==x:
        e-=1
        answer+=1
    elif seq[s]+seq[e]<x:
        s+=1
    else:
        e-=1

print(answer)
            