from heapq import *
def solution(operations):
    minheap=[]
    maxheap=[]
    deleted=[False for _ in range(len(operations))]
    for idx,op in enumerate(operations):
        command,data=op.split()
        if command=="I":
            heappush(minheap,(int(data),idx))
            heappush(maxheap,(-int(data),idx))
        elif command=="D":
            if data=="-1" and minheap:
                d,i=heappop(minheap)
                deleted[i]=True
            elif data=="1" and maxheap:
                d,i=heappop(maxheap)
                deleted[i]=True
        while minheap and deleted[minheap[0][1]]:
            heappop(minheap)
        while maxheap and deleted[maxheap[0][1]]:
            heappop(maxheap)
    answer = [0,0]
    if minheap:
        answer[1]=minheap[0][0]
    if maxheap:
        answer[0]=-maxheap[0][0]
    return answer