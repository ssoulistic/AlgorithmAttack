import sys
input=sys.stdin.readline
N,M=map(int,input().split())
edge=[]
for _ in range(M):
    A,B,C=map(int,input().split())
    edge.append([A-1,B-1,C])

# 1에서 다른 정점으로 갈때의 최단거리들.
answer=False
city=[1e10 for _ in range(N)]
city[0]=0
for v in range(N):
    for start,dest,cost in edge:
        if city[start]!=1e10 and city[dest]>city[start]+cost:
            city[dest]=city[start]+cost
            if v==N-1:
                answer=True

if answer:
    print(-1)
else:
    for i in range(1,N):
        if city[i]==1e10:
            print(-1)
        else:
            print(city[i])