n=int(input())
m=int(input())
computer=list([] for _ in range(n))

for i in range(m):
    p,q=map(int,input().split())
    computer[p-1].append(q-1)
    computer[q-1].append(p-1)

def virus(graph,v,visited):
    visited[v]=True
    for coord in graph[v]:
        if not visited[coord]:
            virus(graph,coord,visited)
    return infected

infected=[False]*(n)
Z=virus(computer,0,infected)
print(Z.count(True)-1)