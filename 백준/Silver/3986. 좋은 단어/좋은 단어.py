import sys
input=sys.stdin.readline
N=int(input())
answer=0
for _ in range(N):
    stack=[]
    for s in input().strip():
        if stack and stack[-1]==s:
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        answer+=1
print(answer)