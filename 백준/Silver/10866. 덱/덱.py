from collections import deque
import sys
n=int(sys.stdin.readline())

class quing():
    def __init__(self):
        self.queue=deque()
    
    def push_front(self,number):
        self.queue.appendleft(number)

    def push_back(self,number):    
            self.queue.append(number)

    def pop_front(self):
        if self.queue:
            print(self.queue.popleft())
        else:
            print(-1)
    
    def pop_back(self):
        if self.queue:
            print(self.queue.pop())
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
    if command[0]=="push_front":
        Q.push_front(command[1])
    elif command[0]=="push_back":
        Q.push_back(command[1])
    elif command[0]=="pop_front":
        Q.pop_front()
    elif command[0]=="pop_back":
        Q.pop_back()
    elif command[0]=="size":
        Q.size()
    elif command[0]=="front":
        Q.front()
    elif command[0]=="back":
        Q.back()
    elif command[0]=="empty":
        Q.empty()
