import sys
n= int(sys.stdin.readline().strip())
stack=[]
for _ in range(n):
    x=int(sys.stdin.readline().strip())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))