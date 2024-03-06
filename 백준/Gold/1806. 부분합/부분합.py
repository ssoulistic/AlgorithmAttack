import sys
input=sys.stdin.readline
N,S=map(int,input().split())
seq=list(map(int,input().split()))
acc=[0]
for i in range(len(seq)):
    acc.append(acc[-1]+seq[i])

s1,s2=0,1
mini=len(acc)
while s2<len(acc):
    if acc[s2]-acc[s1]<S:
        s2+=1
    else:
        mini=min(mini,s2-s1)
        s1+=1
if mini==len(acc):
    print(0)
else:
    print(mini)
    