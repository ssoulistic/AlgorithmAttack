import sys
input=sys.stdin.readline
N=int(input().strip())
graph=[]
answer=0
for _ in range(N):
    graph.append(list(input().strip()))

for k in range(N):
    row_before=""
    col_before=""
    row={"C":0,"P":0,"Z":0,"Y":0}
    col={"C":0,"P":0,"Z":0,"Y":0}
    for l in range(N):
        if row_before==graph[k][l]:
            row[graph[k][l]]+=1
        elif row_before!=graph[k][l]:
            row[graph[k][l]]=1
            row_before=graph[k][l]
        if col_before==graph[l][k]:
            col[graph[l][k]]+=1
        elif col_before!=graph[l][k]:
            col[graph[l][k]]=1
            col_before=graph[l][k]
    answer=max(answer,max(max(row.values()),*col.values()))

search=[[1,0],[0,1]]

for r in range(N):
    for c in range(N):
        for dr,dc in search:
            nr=r+dr
            nc=c+dc
            if 0<=nr<N and 0<=nc<N and graph[nr][nc]!=graph[r][c]:
                graph[nr][nc],graph[r][c]=graph[r][c],graph[nr][nc]
                for k in range(N):
                    row_before=""
                    col_before=""
                    row={"C":0,"P":0,"Z":0,"Y":0}
                    col={"C":0,"P":0,"Z":0,"Y":0}
                    row_max=0
                    col_max=0
                    for l in range(N):
                        if row_before==graph[k][l]:
                            row[graph[k][l]]+=1
                        elif row_before!=graph[k][l]:
                            if row_max<row[graph[k][l]]:
                                row_max=row[graph[k][l]]
                            row[graph[k][l]]=1
                            row_before=graph[k][l]
                    row_max=max(*row.values(),row_max)
                    for l in range(N):
                        if col_before==graph[l][k]:
                            col[graph[l][k]]+=1
                        elif col_before!=graph[l][k]:
                            if col_max<col[graph[l][k]]:
                                col_max=col[graph[l][k]]
                            col[graph[l][k]]=1
                            col_before=graph[l][k]
                    col_max=max(*col.values(),col_max)
                    answer=max(answer,row_max,col_max)
                graph[nr][nc],graph[r][c]=graph[r][c],graph[nr][nc]
print(answer)