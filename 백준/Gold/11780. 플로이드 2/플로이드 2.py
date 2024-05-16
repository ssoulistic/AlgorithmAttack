import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[[1e9,[]] for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i][i][0]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if graph[a-1][b-1][0]>c:
        graph[a-1][b-1][0]=c
        graph[a-1][b-1][1]=[a,b]
        
    
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0]>graph[i][k][0]+graph[k][j][0]:
                graph[i][j][0]=graph[i][k][0]+graph[k][j][0]
                graph[i][j][1]=graph[i][k][1]+graph[k][j][1][1:]
for p in range(n):
    for q in range(n):
        if graph[p][q][0]==1e9:
            graph[p][q][0]=0
        print(graph[p][q][0],end=" ")
    print()

for p in range(n):
    for q in range(n):
        if graph[p][q][0]==0:
            print(0)
        else:
            print(len(graph[p][q][1]),*graph[p][q][1])