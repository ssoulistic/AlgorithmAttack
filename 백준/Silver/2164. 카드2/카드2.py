from collections import deque

q=deque(i for i in range(1,int(input())+1))

while len(q)>1:
    q.popleft()
    if len(q)>1:
        q.append(q.popleft())
print(*q)