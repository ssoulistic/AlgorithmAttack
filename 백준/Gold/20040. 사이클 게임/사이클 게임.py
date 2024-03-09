import sys
input=sys.stdin.readline
n,m=map(int,input().split())
point=[i for i in range(n)]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        point[b]=a
    else:
        point[a]=b

def find(now):
    if now!=point[now]:
        point[now]=find(point[now])
    return point[now]

answer=0
for idx in range(m):
    c,d=map(int,input().split())
    if c>d:
        c,d=d,c
    if find(c)==find(d):
        if answer==0:
            answer=idx+1
    merge(c,d)
print(answer)    