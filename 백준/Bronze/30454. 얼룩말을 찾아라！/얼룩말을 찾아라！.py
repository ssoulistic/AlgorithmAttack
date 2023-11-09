N,M=map(int,input().split())
zebra={}
for _ in range(N):
    black=len(input().replace('0'," ").split())
    if zebra.get(black):
        zebra[black]+=1
    else:
        zebra[black]=1
best=max(map(int,zebra.keys()))
print(best,zebra[best])
