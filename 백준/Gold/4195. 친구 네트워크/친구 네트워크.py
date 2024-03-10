import sys
input=sys.stdin.readline
n=int(input())
def find(name):
    if network[name]!=name:
        network[name]=find(network[name])
    return network[name]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        network[b]=a
        count[a]+=count[b]
        count[b]=0
    elif a>b:
        network[a]=b
        count[b]+=count[a]
        count[a]=0

for _ in range(n):
    F=int(input())
    count={}
    network={}
    for _ in range(F):
        s1,s2=input().split()
        if network.get(s1)==None:
            network[s1]=s1
            count[s1]=1
        if network.get(s2)==None:
            network[s2]=s2
            count[s2]=1
        union(s1,s2)
        print(count[find(s1)])
