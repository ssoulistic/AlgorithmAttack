from collections import deque
def solution(n, wires):
    
    def bfs_and_difference(k):
        graph=[[] for _ in range(n)]
        visited=[False for _ in range(n)]
        for i in range(len(wires)):
            if i!=k:
                s,e=wires[i]
                graph[s-1].append(e-1)
                graph[e-1].append(s-1)
        queue=deque()
        queue.append(0)
        visited[0]=True
        while queue:
            num=queue.popleft()
            for next_num in graph[num]:
                if not visited[next_num]:
                    visited[next_num]=True
                    queue.append(next_num)
        side1=visited.count(True)
        side2=n-side1
        return abs(side1-side2)
    answer = 1e5
    for j in range(len(wires)):
        answer=min(answer,bfs_and_difference(j))
    return answer