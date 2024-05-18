import sys
input=sys.stdin.readline

def find(x):
    if group[x]!=x:
        group[x]=find(group[x])
    return group[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        group[a]=b
        return True
    elif a<b:
        group[b]=a
        return True
    return False

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    group=[i for i in range(N)]
    answer=0
    for _ in range(M):
        a,b=map(int,input().split())
        x=union(a-1,b-1)
        if x:
            answer+=1
    print(answer)