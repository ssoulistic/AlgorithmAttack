def solution(n, computers):
    visited=[False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            answer+=1
            que=[]
            que.append(i)
            while que:
                next=que.pop(0)
                for j in range(i+1,len(computers[next])):
                    if computers[next][j]==1 and not visited[j]:
                        visited[j]=True
                        que.append(j)
    return answer