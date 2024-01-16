import sys
input=sys.stdin.readline
import heapq
N=int(input())
M=int(input())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b,cost=map(int,input().split())
    graph[a-1].append([b-1,cost])
start,end=map(int,input().split())

def dikstra(dep,arr):
    pay=[10**8 for _ in range(N)]
    que=[]
    pay[dep]=0
    heapq.heappush(que,[pay[dep],dep])
    while que:
        cur_pay,dest=heapq.heappop(que)
        if pay[dest]<cur_pay:
            continue
        for next,costt in graph[dest]:
            if pay[next]>pay[dest]+costt:
                pay[next]=pay[dest]+costt
                heapq.heappush(que,[costt,next])
    return pay[arr]
print(dikstra(start-1,end-1))