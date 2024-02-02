import sys
input=sys.stdin.readline
import heapq
N=int(input())
cards=[]
for _ in range(N):
    cards.append(int(input()))
count=0
heapq.heapify(cards)
while len(cards)>1:
    a=heapq.heappop(cards)
    b=heapq.heappop(cards)
    count+=(a+b)
    heapq.heappush(cards,a+b)
print(count)
