from collections import deque
def solution(n, wires):
    # 한개씩 빼보면서.. bfs일까.
    
    def bfs(k):
        graph=[[] for _ in range(n)]
        visited=[False for _ in range(n)]
        for i in range(len(wires)):
            if i!=k: # k번째만 스킵
                graph[wires[i][0]-1].append(wires[i][1]-1)
                graph[wires[i][1]-1].append(wires[i][0]-1)
        que=deque()
        visited[0]=True
        que.append(0)
        while que:
            next=que.popleft()
            for g in graph[next]:
                if not visited[g]:
                    visited[g]=True
                    que.append(g)
        result=visited.count(True)-visited.count(False)
        return abs(result)
    answer = n
    for i in range(n):
        diff=bfs(i)
        if answer>diff:
            answer=diff
    return answer
