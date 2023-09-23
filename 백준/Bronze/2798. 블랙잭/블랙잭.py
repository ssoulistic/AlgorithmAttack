from itertools import combinations
n,k=map(int,input().split())
l=list(map(int,input().split()))
answer=0
for x,y,z in combinations(l,3):
    if x+y+z<=k and answer<x+y+z:
        answer=x+y+z
print(answer)