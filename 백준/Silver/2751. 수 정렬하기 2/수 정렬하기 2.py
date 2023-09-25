import sys
n=int(sys.stdin.readline())
l=[]
for _ in range(n):
    l.append(int(sys.stdin.readline()))
for num in sorted(l):
    print(num)