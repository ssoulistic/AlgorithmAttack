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

V,E=map(int,input().split())
group=[i for i in range(V)]
queue=[]
for _ in range(E):
    A,B,C=map(int,input().split())
    queue.append([-C,[A,B]])
queue.sort()
answer=0
while queue:
    cost,[start,end]=queue.pop()
    if union(start-1,end-1):
        answer-=cost
print(answer)