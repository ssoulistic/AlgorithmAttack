import sys
input=sys.stdin.readline

N=int(input())
players=list(map(int,input().split()))
check=[False for _ in range(1000001)]
dic={}
for l in players:
    check[l]=True
    dic[l]=0

for p in range(N):
    i=2
    while players[p]*i<1000001:
        if check[players[p]*i]:
            dic[players[p]]+=1
            dic[players[p]*i]-=1
        i+=1
for q in range(N):
    print(dic[players[q]],end=" ")