def solution(N, road, K):
    import heapq
    graph=[[] for _ in range(N)]
    time=[1e9 for _ in range(N)]
    time[0]=0
    for s,e,cost in road:
        graph[s-1].append([e-1,cost])
        graph[e-1].append([s-1,cost])
    
    def dijkstra(start):
        que=[]
        heapq.heappush(que,[0,start])
        while que:
            t,where=heapq.heappop(que)
            if time[where]<t:
                continue
            for dest,value in graph[where]:
                if time[dest]>time[where]+value:
                    time[dest]=time[where]+value
                    heapq.heappush(que,[time[dest],dest])
    dijkstra(0)    
    
    answer = 0          
    for t in time:
        if t<=K:
            answer+=1
    return answer