import sys
input=sys.stdin.readline
from heapq import *
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,cost=map(int,input().split())
    graph[s].append([e,cost])
ts,te=map(int,input().split())

def dijkstra(Spoint):
    cost_map=[[1e10,[]] for _ in range(n+1)]
    cost_map[Spoint]=[0,[Spoint]]
    route=[Spoint]
    queue=[[0,Spoint,route]]
    heapify(queue)
    while queue:
        acc,next,route=heappop(queue)
        if acc>cost_map[next][0]:
            continue
        for next_destination,next_cost in graph[next]:
            if cost_map[next_destination][0]>next_cost+acc:
                cost_map[next_destination]=[next_cost+acc,route+[next_destination]]
                heappush(queue,[cost_map[next_destination][0],next_destination,route+[next_destination]])
    return cost_map
c,r=dijkstra(ts)[te]
print(c)
print(len(r))
print(*r)