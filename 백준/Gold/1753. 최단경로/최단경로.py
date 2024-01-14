import sys
input=sys.stdin.readline
import heapq
V,E=map(int,input().split()) # 정점과 간선 수
K=int(input())-1 #시작 정점
graph=[[] for _ in range(V)]
for _ in range(E):
    u,v,w=map(int,input().split()) # u 에서 v로 가는 가중치w인 간선
    graph[u-1].append((v-1,w))

# K 시작하여 각 정점의 최적값.
end=["INF" for _ in range(V)]
que=[]
end[K]=0
heapq.heappush(que,[end[K],K])
while que:
    end_next,next=heapq.heappop(que)
    if end[next]<end_next:
        continue
    for node,weight in graph[next]:
        if end[node]!="INF":
            if end[node]>end[next]+weight:
                end[node]=end[next]+weight
                heapq.heappush(que,[end[node],node])
        else:
            end[node]=end[next]+weight
            heapq.heappush(que,[end[node],node])
    
for e in end:
    print(e)