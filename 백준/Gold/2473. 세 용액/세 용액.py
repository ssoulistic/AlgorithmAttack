import sys
input=sys.stdin.readline
N=int(input())
liq=list(map(int,input().split()))
liq.sort()
minimum=1e10
memo=[]

for a in range(N):
    for b in range(a+1,N):
        s=b+1
        e=N-1
        while s<e<N:
            mid=(s+e)//2
            if liq[a]+liq[b]+liq[mid]<0:
                s=mid+1
            else:
                e=mid
        if a<b<e and  minimum>abs(liq[a]+liq[b]+liq[e]):
            minimum=abs(liq[a]+liq[b]+liq[e])
            memo=[a,b,e]
        if a<b<e-1 and  minimum>abs(liq[a]+liq[b]+liq[e-1]):
            minimum=abs(liq[a]+liq[b]+liq[e-1])
            memo=[a,b,e-1]

print(*map(lambda x: liq[x],memo))
