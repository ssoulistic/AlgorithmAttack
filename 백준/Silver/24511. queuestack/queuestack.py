from collections import deque
import sys
n=int(sys.stdin.readline())
sq=sys.stdin.readline().split()
comp=sys.stdin.readline().split()
m=int(sys.stdin.readline())
i=sys.stdin.readline().split()
answer=deque()
for k in range(n):
    if sq[k]=="0":
        answer.append(comp[k])
for num in i:
    answer.appendleft(num)
    print(answer.pop(),end=" ")