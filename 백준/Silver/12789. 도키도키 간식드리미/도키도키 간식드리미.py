import sys
from collections import deque
n=int(sys.stdin.readline())
queue=deque(map(int,sys.stdin.readline().split()))
wait=deque()
turn=1
result='Nice'
while queue or wait:
    if queue and queue[0]==turn:
        queue.popleft()
        turn+=1
    elif wait and wait[0]==turn:
        wait.popleft()
        turn+=1
    elif not queue:
        if wait[0]!=turn:
            result="Sad"
            break
        else:
            wait.popleft()
            turn+=1
    else:
        wait.appendleft(queue.popleft())
print(result)