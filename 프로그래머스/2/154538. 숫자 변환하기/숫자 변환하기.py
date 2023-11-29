from collections import deque
def solution(x, y, n):
    if x==y:
        return 0
    visited=[-1 for _ in range(y+1)]
    que=deque()
    search=[f"+{n}","*2","*3"]
    def bfs(r):
        visited[r]=0
        que.append(r)
        while que:
            next=que.popleft()
            for s in search:
                z=eval(str(next)+s)
                if 0<=z<=y and visited[z]==-1:
                    visited[z]=visited[next]+1
                    if z!=y:
                        que.append(z)
                    else:
                        return
    bfs(x)
    if visited[y]:
        return visited[y]
    else:
        return -1
