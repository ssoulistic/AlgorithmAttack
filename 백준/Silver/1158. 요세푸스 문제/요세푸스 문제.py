from collections import deque
n,k=map(int,input().split())
yose=deque(i for i in range(1,n+1))
answer=[]
while yose:
    for j in range(k-1):
        yose.append(yose.popleft())
    answer.append(yose.popleft())
print(f'<{", ".join(map(str,answer))}>')