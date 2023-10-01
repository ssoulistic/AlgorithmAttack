from collections import deque
import sys
n=int(sys.stdin.readline())

class quing():
    def __init__(self):
        self.queue=deque()
    
    def push(self,number):
        self.queue.append(number)

    def pop(self):
        if self.queue:
            print(self.queue.popleft())
        else:
            print(-1)

    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if self.queue:
            print(0)
        else:
            print(1)
    
    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)
    
    def back(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)
    
Q=quing()
for _ in range(n):
    command=sys.stdin.readline().split()
    if command[0]=="push":
        Q.push(command[1])
    elif command[0]=="pop":
        Q.pop()
    elif command[0]=="size":
        Q.size()
    elif command[0]=="front":
        Q.front()
    elif command[0]=="back":
        Q.back()
    elif command[0]=="empty":
        Q.empty()
