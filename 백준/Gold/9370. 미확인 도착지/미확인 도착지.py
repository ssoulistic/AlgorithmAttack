import sys
input=sys.stdin.readline
# 다익스트라 경로로 목적지 어딘가로 가는경우의 경로중 도로를 지나는 경우
# 1. start to 목적지 경로 모두 구하기
# 2. 경로 나온것 중 도로가 포함되는지 구하여 제출
T=int(input())
from heapq import *

def dijkstra(start,town_map):
    distance=[1e9 for _ in range(len(town_map))]
    distance[start]=0
    queue=[]
    queue.append([0,start,[start]])
    heapify(queue)
    while queue:
        acc_distance,now,history=heappop(queue)
        if acc_distance>distance[now]:
            continue
        for next_town,next_distance in town_map[now]:
            if distance[next_town]>distance[now]+next_distance:
                distance[next_town]=distance[now]+next_distance
                heappush(queue,[distance[next_town],next_town,history+[next_town]])
    return distance


for _ in range(T):
    n,m,t=map(int,input().split()) # n 교차로수 도로 수 목적지 후보수
    s,g,h=map(int,input().split()) # s 출발지 g,h 도로
    answer=[]
    graph=[[] for _ in range(n)]
    suspicious=[]
    gtoh=0
    for _ in range(m):
        a,b,d=map(int,input().split())
        graph[a-1].append([b-1,d])
        graph[b-1].append([a-1,d])
        if (a==g and b==h) or (a==h and b==g):
            gtoh=d
    for _ in range(t):
        x=int(input())
        suspicious.append(x)
    distance_from_s=dijkstra(s-1,graph)
    distance_from_g=dijkstra(g-1,graph)
    distance_from_h=dijkstra(h-1,graph)

    for sus in suspicious:
        if distance_from_s[g-1]+gtoh+distance_from_h[sus-1]==distance_from_s[sus-1] or distance_from_s[h-1]+gtoh+distance_from_g[sus-1]==distance_from_s[sus-1]:
            answer.append(sus)
    print(*sorted(answer))