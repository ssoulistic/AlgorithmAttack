from collections import deque
def solution(places):
    answer=[]
    def smallbfs(start,graph):
        visited=[[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
        visited[start[0]][start[1]]=1
        que=deque()
        que.append(start)
        search=[[-1,0],[1,0],[0,-1],[0,1]]
        while que:
            ri,ci=que.popleft()
            for dr,dc in search:
                nr=ri+dr
                nc=ci+dc
                if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc]:
                    if graph[nr][nc]=="P":
                        if visited[ri][ci]<3:
                            return 0
                        else:
                            visited[nr][nc]=visited[ri][ci]+1
                    elif graph[nr][nc]=="O":
                        que.append([nr,nc])
                    visited[nr][nc]=visited[ri][ci]+1
                        
        return 1
            
    for p in places:
        result=1
        for row in range(len(p)):
            for col in range(len(p[0])):
                if p[row][col]=="P":
                    x=smallbfs([row,col],p)
                    if not x:
                        result=0
                        break
        answer.append(result)
    return answer