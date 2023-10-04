import sys
memo={}
n,m=map(int,sys.stdin.readline().split())
for _ in range(n):
    word=sys.stdin.readline().rstrip()
    if len(word)>=m:
        if memo.get(word):
            memo[word]+=1
        else:
            memo[word]=1

prio=[]
for k,v in memo.items():
    prio.append([k,v])
prio.sort(key=lambda x: (-x[1],-len(x[0]),x[0]))
for p in prio:
    print(p[0])