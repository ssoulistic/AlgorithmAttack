import sys
input=sys.stdin.readline
x=int(input())
for _ in range(9):
    x-=int(input())
print(x)