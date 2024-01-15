import sys
input=sys.stdin.readline
import heapq
N,M,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,T=map(int,input().split())
    graph[a].append([b,T])

def dikstra(start,end):
    que=[]
    time=[10**7 for _ in range(N+1)]
    time[start]=0
    heapq.heappush(que,[time[start],start])
    while que:
        acc_time,curr=heapq.heappop(que)
        if time[curr]<acc_time:
            continue
        for next,next_time in graph[curr]:
            if next_time+acc_time<time[next]:
                time[next]=next_time+acc_time
                heapq.heappush(que,[time[next],next])
    return time[end]
answer=0
for i in range(1,N+1):
    distance=dikstra(i,X)+dikstra(X,i)
    if answer<distance:
        answer=distance
print(answer)