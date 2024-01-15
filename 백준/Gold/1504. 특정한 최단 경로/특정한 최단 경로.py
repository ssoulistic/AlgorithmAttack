import sys
input=sys.stdin.readline
import heapq
N,E=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])
v1,v2=map(int,input().split())
# 시작=> 1=> 임의의 점 2개 순서별 => N
# 1,v1 v1,v2 v2,N
# 1,v2 v2,v1 v1,N

def dikstra(start,end):
    weighted=[1000*200000+1 for _ in range(N)]
    weighted[start]=0
    que=[]
    heapq.heappush(que,(weighted[start],start)) # 시작지점의 거리, 위치
    # 가장 거리 짧은것 부터, 긴것은 계산할 필요x
    while que:
        cur_w,cur=heapq.heappop(que)
        if weighted[cur]<cur_w:
            continue
        for node,weight in graph[cur]:
            if weighted[node]>weighted[cur]+weight:
                weighted[node]=weighted[cur]+weight
                heapq.heappush(que,[weighted[node],node])
    return weighted[end]

route1=dikstra(0,v1-1)+dikstra(v1-1,v2-1)+dikstra(v2-1,N-1)
route2=dikstra(0,v2-1)+dikstra(v2-1,v1-1)+dikstra(v1-1,N-1)
if route1>=1000*200000+1 and route2>=1000*200000+1:
    print(-1)
else:
    print(min(route1,route2))