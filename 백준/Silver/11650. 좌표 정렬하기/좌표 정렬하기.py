import sys
n=int(sys.stdin.readline())
l=[]
for _ in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))
l.sort()
for k in l:
    print(k[0],k[1])