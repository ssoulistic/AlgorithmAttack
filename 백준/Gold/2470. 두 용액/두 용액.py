import sys
input=sys.stdin.readline
N=int(input())
liquid=sorted(map(int,input().split()))

s=0
e=len(liquid)-1
mini=1e10
pair=[]
while s<e:
    if abs(liquid[s]+liquid[e])<=mini:
        mini=abs(liquid[s]+liquid[e])
        pair=[s,e]
    if abs(liquid[s])<abs(liquid[e]):
        e-=1
    else:
        s+=1
print(liquid[pair[0]],liquid[pair[1]])