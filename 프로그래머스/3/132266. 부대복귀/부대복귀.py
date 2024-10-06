from heapq import *
def solution(n, roads, sources, destination):
    graph=[[] for _ in range(n)]
    for ra,rb in roads:
        graph[ra-1].append(rb-1)
        graph[rb-1].append(ra-1)
    costs=[float('inf')]*n
    def dijkstra(start):
        costs[start]=0
        queue=[]
        heappush(queue,(0,start))
        while queue:
            acc,curr=heappop(queue)
            if costs[curr]<acc:
                continue
            for nxt in graph[curr]:
                if costs[nxt]>acc+1:
                    costs[nxt]=acc+1
                    heappush(queue,(acc+1,nxt))
                    
    dijkstra(destination-1)
    answer = []
    for s in sources:
        if costs[s-1]==float('inf'):
            answer.append(-1)
        else:
            answer.append(costs[s-1])
    return answer