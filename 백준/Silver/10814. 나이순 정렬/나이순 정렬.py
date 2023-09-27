import sys
n=int(sys.stdin.readline())
members=[]
for _ in range(n):
    x,y=sys.stdin.readline().split()
    members.append([int(x),y])
members.sort(key=lambda x : x[0])
for mem in members:
    print(*mem)