from collections import deque
T=int(input())
for _ in range(T):
    numbers,target=map(int,input().split())
    Q=list(map(int,input().split()))
    idx=list(i for i in range(len(Q)))
    Q = deque(zip(Q,idx))
    count=0
    while True:
        while Q[0][0]!=max(Q)[0]:
            Q.append(Q.popleft())
        count+=1
        x=Q.popleft()
        if x[1]==target:
            break
    print(count)


