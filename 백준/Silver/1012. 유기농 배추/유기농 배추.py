from collections import deque
T=int(input())
que=deque()
search=[[1,0],[-1,0],[0,1],[0,-1]]
def bfs(gp,x,y):
    if not visited[y][x]:
        visited[y][x]=True
        que.append([x,y])
        
        while que:
            ground=que.pop()
            for s in search:
                x1=ground[0]+s[0]
                y1=ground[1]+s[1]
                if 0<=x1<=M-1 and 0<=y1<=N-1 and not visited[y1][x1]:
                    visited[y1][x1]=True
                    que.append([x1,y1])
        return True
    else:
        return False
    
for _ in range(T):
    M,N,K=map(int,input().split()) #가로 세로 위치 개수.
    graph=[[0 for _ in range(M)] for _ in range(N)]
    visited=[[True for _ in range(M)] for _ in range(N)]
    count=0
    for _ in range(K):
        x1,y1=map(int,input().split()) 
        graph[y1][x1]=1
        visited[y1][x1]=False
    for p in range(M):
        for q in range(N):
            if bfs(graph,p,q):
                count+=1
    print(count)
    