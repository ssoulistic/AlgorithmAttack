import sys
input=sys.stdin.readline
from heapq import *
N,K=map(int,input().split())
jewels=[]
for _ in range(N):
    M,V=map(int,input().split())
    jewels.append([M,V])

bags=[]
for _ in range(K):
    C=int(input())
    bags.append(C)

bags.sort()
jewels.sort()
answer=0
cand=[]

for bag in bags:
    while jewels and jewels[0][0]<=bag:
        heappush(cand,-jewels[0][1])
        heappop(jewels)
    if cand:
        answer-=heappop(cand)
print(answer)