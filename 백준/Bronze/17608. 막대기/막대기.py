import sys
n=int(sys.stdin.readline())
stack=[]
for _ in range(n):
    stack.append(int(sys.stdin.readline()))
max=0
count=0
for _ in range(n):
    x=stack.pop()
    if max<x:
        max=x
        count+=1
print(count)