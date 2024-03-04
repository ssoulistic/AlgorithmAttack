import sys
input=sys.stdin.readline

K=int(input())
team=["A","B"]
def bfs(start):
    if color[start]!=False:
        return True
    color[start]=team[0]
    que=[]
    que.append([start,1])
    while que:
        edge,tn=que.pop(0)
        for next in graph[edge]:
            if color[next]==False:
                color[next]=team[tn]
                que.append([next,(tn+1)%2])
            elif color[next]!=team[tn]:
                    return False
    return True

for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V)]
    color=[False for _ in range(V)]
    answer="YES"
    for _ in range(E):
        a,b=map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(V):
        check=(bfs(i))
        if not check:
            answer="NO"
            break
    print(answer)
