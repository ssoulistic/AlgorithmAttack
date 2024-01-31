import sys
input=sys.stdin.readline
N=int(input())
S=input()
bulb=[]

for ch in S:
    if ch=="R":
        bulb.append(0)
    elif ch=="G":
        bulb.append(1)
    elif ch=="B":
        bulb.append(2)

answer=3**N
for t in range(3): # t = target
    temp=bulb.copy()
    count=0
    for i in range(N-2):
        change=(t-temp[i])%3
        count+=change
        for j in range(3):
            temp[i+j]+=change
            temp[i+j]%=3
    if all (t==n for n in temp):
        if answer>count:
            answer=count
if answer!=3**N:
    print(answer)
else:
    print(-1)