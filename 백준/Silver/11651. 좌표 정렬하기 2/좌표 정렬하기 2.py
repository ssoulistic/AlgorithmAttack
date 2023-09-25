import sys
n=int(sys.stdin.readline())
l=[]
for _ in range(n):
    x=list(map(int,sys.stdin.readline().split()))
    l.append([x[1],x[0]])
l.sort()
for k in l:
    print(k[1],k[0])