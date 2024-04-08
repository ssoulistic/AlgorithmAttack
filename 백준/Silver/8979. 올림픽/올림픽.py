import sys
input=sys.stdin.readline
N,K=map(int,input().split())
ranking=[[] for _ in range(N)]
target=[]
for _ in range(N):
    country,*medals=map(int,input().split())
    ranking[country-1]=medals
    if country==K:
        target=medals
ranking.sort(reverse=True)
for r in range(N):
    if ranking[r]==target:
        print(r+1)
        break
