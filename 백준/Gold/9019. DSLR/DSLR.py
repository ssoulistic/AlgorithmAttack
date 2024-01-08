import sys
T=int(sys.stdin.readline())
def regi(n,command):
    if command=="D":
        n*=2
        n%=10000
        return n
    elif command=="S":
        n-=1
        if n<0:
            n+=10000
        return n
    elif command=="L":
        return (n%1000)*10+n//1000
    elif command=="R":
        return (n%10)*1000+n//10
        

from collections import deque
def check(n1):
    commands="DSLR"
    results=[False for _ in range(10000)]
    que=deque()
    results[n1]=""
    que.append(n1) 
    while que:
        next=que.popleft()
        if next==B:
            return results[next]
        for com in commands:
            x=regi(next,com)
            if results[x]==False:
                results[x]=results[next]+com
                que.append(x)

for _ in range(T):
    A,B=map(int,sys.stdin.readline().split())
    print(check(A))