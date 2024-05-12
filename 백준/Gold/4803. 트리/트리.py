import sys
input=sys.stdin.readline  
case=1
def find(num):
    if uf[num]!=num:
        uf[num]=find(uf[num])
    return uf[num]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        uf[b]=a
        if tree.get(b)==False:
            tree[a]=False
    else:
        uf[a]=b
        if tree.get(a)==False:
            tree[b]=False

while True:
    n,m=map(int,input().split())
    tree={}
    uf=[i for i in range(n)]
    if n==0 and m==0:
        break
    for _ in range(m):
        p,q=map(int,input().split())
        if find(p-1)==find(q-1):
            tree[find(p-1)]=False
        else:
            union(p-1,q-1)

    answer=0
    for gn in uf:
        if tree.get(find(gn))==None:
            tree[find(gn)]=True
            answer+=1
    if answer>1:
        print(f"Case {case}: A forest of {answer} trees.")
    elif answer==1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: No trees.")
    case+=1