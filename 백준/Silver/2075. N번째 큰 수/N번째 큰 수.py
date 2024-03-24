import sys
input=sys.stdin.readline
from heapq import *
N=int(input())
que=[]
for num in list(map(int,input().split())):
        heappush(que,num)
for _ in range(N-1):
    for num in list(map(int,input().split())):
        heappush(que,num)
        heappop(que)
x=heappop(que)
print(x)
