import sys
input=sys.stdin.readline
N,K=map(int,input().split())
import heapq
graph=[1e10 for _ in range(2*N+2*K)]
def dikstra(count):
    que=[]
    heapq.heappush(que,[count,N])
    while que:
        time,curr=heapq.heappop(que)
        if curr==K:
            return time
        if 0<=curr<len(graph):
            if graph[curr]<time:
                continue
            elif graph[curr]==1e10:
                graph[curr]=time
                if 0<=2*curr<len(graph):
                    heapq.heappush(que,[time,2*curr])
                if 0<=curr-1<len(graph):
                    heapq.heappush(que,[time+1,curr-1])
                if 0<=curr+1<len(graph):
                    heapq.heappush(que,[time+1,curr+1])
        
print(dikstra(0))