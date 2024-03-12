import sys
input=sys.stdin.readline
V,E=map(int,input().split())
graph=[[1e9 for _ in range(V)] for _ in range(V)]
for _ in range(E):
    a,b,c=map(int,input().split())
    graph[a-1][b-1]=c
for via in range(V):
    for depart in range(V):
        for destination in range(V):
            graph[depart][destination]=min(graph[depart][via]+graph[via][destination],graph[depart][destination])
answer=1e9
for i in range(V):
    if answer>graph[i][i]:
        answer=graph[i][i]
if answer==1e9:
    print(-1)
else:
    print(answer)
        