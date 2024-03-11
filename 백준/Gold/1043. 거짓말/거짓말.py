import sys
input=sys.stdin.readline
N,M=map(int,input().split())
t,*truth=map(int,input().split())
group=[i for i in range(N)]
party=[]

def find(a):
    if group[a]!=a:
            group[a]=find(group[a])
    return group[a]

def union(gp):
    root=min(map(find,gp))
    for g in gp:
        if group[g]==g:
            group[g]=root
        else:
            group[group[g]]=root

# 그룹화 => 진실파티, 거짓파티
for _ in range(M):
    p,*par=map(int,input().split())
    par=list(map(lambda x: x-1,par))
    party.append(par)
    union(par)

tp=[False for _ in range(N)]
for t in truth:
     tp[find(t-1)]=True


# 각 파티의 참석자에 따라 파티가 자연스레 나뉨.
lie=0
for p in party:
     if all(False if tp[j] else True for j in map(find,p)):
            lie+=1

print(lie)