import sys
n=int(sys.stdin.readline())
l=[0 for _ in range(10001)]
for _ in range(n):
    l[int(sys.stdin.readline())]+=1
for idx,num in enumerate(l):
    for _ in range(num):
        print(idx)