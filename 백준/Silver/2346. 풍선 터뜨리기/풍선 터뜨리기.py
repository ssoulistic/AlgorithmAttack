from collections import deque
n=int(input())
move=list(map(int,input().split()))
bal=deque(range(1,n+1))
for _ in range(n):
    m=bal.popleft()
    next=move[m-1]
    print(m,end=" ")
    if bal:
        if next>0:
            for _ in range(next-1):
                bal.append(bal.popleft())
        if next<0:
            for _  in range(-next):
                bal.appendleft(bal.pop())