import heapq
import sys
heap=[]
T=int(sys.stdin.readline())
for _ in range(T):
    x=int(sys.stdin.readline())
    if x==0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        if x<0:
            heapq.heappush(heap,(-x,x))
        else:
            heapq.heappush(heap,(x,x))
