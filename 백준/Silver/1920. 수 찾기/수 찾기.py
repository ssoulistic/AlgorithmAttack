import sys
n=int(sys.stdin.readline())
l=set(sys.stdin.readline().split())
m=int(sys.stdin.readline())
k=list(sys.stdin.readline().split())
for search in k:
    if search in l:
        print(1)
    else:
        print(0)