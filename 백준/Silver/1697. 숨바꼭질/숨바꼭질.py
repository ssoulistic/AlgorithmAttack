from collections import deque
N,K=map(int,input().split())
limit=max(N,K)*2
graph=[False for _ in range(limit+1)]
que=deque()
search=["-1","+1","*2"]
def bfs(n):
    graph[n]=1
    que.append(n)
    while que:
        next=que.popleft()
        for s in search:
            l=eval(str(next)+s)
            if 0<=l<=limit and not graph[l]:
                graph[l]=graph[next]+1
                que.append(l)

bfs(N)
print(graph[K]-1)