import sys
input=sys.stdin.readline
N,score,P=map(int,input().split())
rank=[-1 for _ in range(P)]
answer=-1
for idx,val in enumerate(map(int,input().split())):
  rank[idx]=val
for i in range(P):
  if rank[i]<=score and rank[-1]<score:
    answer=i+1
    break
print(answer)