from collections import deque
def solution(maps):
    row=len(maps)
    col=len(maps[0])
    v1=[[0 for _ in range(col)] for _ in range(row)]
    v2=[[0 for _ in range(col)] for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if maps[r][c]!="X":
                v1[r][c]=False
                v2[r][c]=False
                if maps[r][c]=="S":
                    s=[r,c]
                elif maps[r][c]=="L":
                    m=[r,c]
                elif maps[r][c]=="E":
                    e=[r,c]

    def bfs(start,end,visited):
        r1,c1=start
        visited[r1][c1]=1
        que=deque()
        que.append([r1,c1])
        search=[[-1,0],[0,-1],[1,0],[0,1]]
        while que:
            r2,c2=que.popleft()
            for dr,dc in search:
                nr=dr+r2
                nc=dc+c2
                if 0<=nr<row and 0<=nc<col and maps[nr][nc]!="X":
                    if not visited[nr][nc]:
                        visited[nr][nc]=visited[r2][c2]+1
                        que.append([nr,nc])
                    elif visited[nr][nc]>visited[r2][c2]+1:
                        visited[nr][nc]=visited[r2][c2]+1
                        que.append([nr,nc])
        return visited[end[0]][end[1]] 
    x=bfs(s,m,v1)
    y=bfs(m,e,v2)
    if x and y:
        answer=(x-1+y-1)
    else:
        answer=(-1)
    return answer