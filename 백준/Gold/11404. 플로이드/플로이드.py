import sys
input=sys.stdin.readline
n=int(input()) #도시 수
m=int(input()) #버스의 수
table=[[1e9 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c=map(int,input().split())
    table[a-1][b-1]=min(table[a-1][b-1],c)

for i in range(n):
     table[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):                
            table[i][j]=min(table[i][j],table[i][k]+table[k][j])
for i in range(n):
    for j in range(n):
        if table[i][j]==1e9:
            table[i][j]=0    
for t in table:
     print(*t)


