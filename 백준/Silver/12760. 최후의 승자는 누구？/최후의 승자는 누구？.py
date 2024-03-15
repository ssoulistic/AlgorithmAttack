import sys
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[]
point=[0 for _ in range(N)]
for _ in range(N):
    graph.append(sorted(map(int,input().split()),reverse=True))
for turn in range(M):
    temp=[]
    for idx in range(N):
        temp.append(graph[idx][turn])
    win=max(temp)
    for i in range(N):
        if temp[i]==win:
            point[i]+=1
winner=max(point)
answer=[]
for j in range(N):
    if point[j]==winner:
        answer.append(j+1)
    
    
print(*answer)        
    

