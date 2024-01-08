import heapq
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    k=int(input())
    maxheap=[]
    minheap=[]
    deleted=[False]*k
    for idx in range(k):
        command,n=input().split()
        if command=="I": # n 값 삽입
            heapq.heappush(minheap,(int(n),idx))
            heapq.heappush(maxheap,(-int(n),idx))
        elif command=="D":
            if n =="1": #최대값 삭제
                if maxheap:
                    deleted[maxheap[0][1]]=True
            elif n=="-1": #최소값 삭제
                if minheap:
                    deleted[minheap[0][1]]=True
        while maxheap and deleted[maxheap[0][1]]:
            heapq.heappop(maxheap)
        while minheap and deleted[minheap[0][1]]:
            heapq.heappop(minheap)
    if minheap and maxheap:
        print(-maxheap[0][0],minheap[0][0])
    else:
        print("EMPTY")