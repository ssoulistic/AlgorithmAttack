import sys
input=sys.stdin.readline
hooroo={}
for i in range(9):
  hooroo[i+1]=0
N=int(input())
fruits=list(map(int,input().split()))
s,e=0,0
type_count=0
answer=0

for e in range(N):
  if hooroo[fruits[e]]==0:
    type_count+=1
  hooroo[fruits[e]]+=1
  
  if type_count>2:
    while type_count>2:
      hooroo[fruits[s]]-=1
      if hooroo[fruits[s]]==0:
        type_count-=1
      s+=1
  answer=max(answer,e-s+1)
print(answer)
    