import sys
input=sys.stdin.readline
R,C=map(int,input().split())
graph=[]
answer=0
for _ in range(R):
    graph.append(list(input().strip()))
alpha=[False for _ in range(26)]

def dfs(coord,count):
    global answer 
    r,c=coord
    idx_now=ord(graph[r][c])-ord("A")
    answer=max(answer,count)
    
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr=r+dr
        nc=c+dc
        if 0<=nr<R and 0<=nc<C and not alpha[ord(graph[nr][nc])-ord("A")]:
            alpha[ord(graph[nr][nc])-ord("A")]=True
            dfs([nr,nc],count+1)
            alpha[ord(graph[nr][nc])-ord("A")]=False

alpha[ord(graph[0][0])-ord("A")]=True
dfs([0,0],1)
print(answer)