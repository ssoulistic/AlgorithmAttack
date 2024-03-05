import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
group=[i for i in range(n+1)]


def union(c,d):
    c=find(group[c])
    d=find(group[d])
    if c<d:
        group[d]=c
    else:
        group[c]=d
    
def find(c):
    if group[c]!=c:
        group[c]=find(group[c])
    return group[c]

def check(c,d):
    c=find(c)
    d=find(d)
    if c==d:
        return True
    else:
        return False
    
for _ in range(m):
    command,a,b=map(int,input().split())
    if command==1:
        if check(a,b):
            print("YES")
        else:
            print("NO")
        # a,b가 같은 집합에 포함되는지 check 
        # 포함시 yes 아니면 no
    elif command==0:
        if a!=b:
            union(a,b)
            # a와 b 집합 합치기.