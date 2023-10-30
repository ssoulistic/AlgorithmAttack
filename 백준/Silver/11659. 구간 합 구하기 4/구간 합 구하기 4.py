import sys
N,M=map(int,sys.stdin.readline().split())
pool=list(map(int,sys.stdin.readline().split()))
answer=[0]
for l in range(N):
    if answer:
        answer.append(answer[-1]+pool[l])
for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print(answer[j]-answer[i-1])