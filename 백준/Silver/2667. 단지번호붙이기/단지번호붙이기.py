from collections import deque
T=int(input())
mura=[]
visited=[[False for _ in range(T)] for _ in range(T)]
graph=[[0 for _ in range(T)] for _ in range(T)]
que=deque()
search=[[-1,0],[1,0],[0,-1],[0,1]]
def bfs(G,x,y):
    if not visited[x][y]:
        count=1
        visited[x][y]=True
        que.append([x,y])
        while que:
            next=que.popleft()
            for s in search:
                x1 = next[0]+s[0]
                y1 = next[1]+s[1]
                if 0<=x1<T and 0<=y1<T and graph[x1][y1]==1 and not visited[x1][y1]:
                    count+=1
                    que.append([x1,y1])
                    visited[x1][y1]=True
        return count
    else:
        return False    
    
for i in range(T):
    line=input()
    for j in range(T):
        graph[i][j]=int(line[j])
        if line[j]=="0":
            visited[i][j]=True     
    
for p in range(T):
     for q in range(T):
         x=bfs(graph,p,q)
         if x:
             mura.append(x)
print(len(mura))
for l in sorted(mura):
    print(l)