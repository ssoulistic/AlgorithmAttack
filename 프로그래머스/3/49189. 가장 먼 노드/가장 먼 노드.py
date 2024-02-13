def solution(n, edge):
    import heapq
    graph=[[] for _ in range(n)]
    dist=[1e8 for _ in range(n)]
    for s,e in edge:
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
    que=[]
    dist[0]=0
    heapq.heappush(que,[0,0])
    while que:
        now,far=heapq.heappop(que)
        if dist[now]>far:
            continue
        for nt in graph[now]:
            if dist[nt]!=1e8:
                if dist[nt]>dist[now]+1:
                    dist[nt]=dist[now]+1
                    heapq.heappush(que,[nt,dist[nt]])
            else:
                dist[nt]=dist[now]+1
                heapq.heappush(que,[nt,dist[nt]])
    c=max(dist)
    answer=dist.count(c)
    return answer