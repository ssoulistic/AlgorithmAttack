import sys
input=sys.stdin.readline
N,M=map(int,input().split())
seq=sorted(map(int,input().split()))
answer=[]
stack=[]
def backt(k):    
    for i in range(k,N):
        stack.append(seq[i])
        if len(stack)==M:
            if stack not in answer:
                answer.append(stack[:])
        backt(i+1)
        stack.pop()
    return
backt(0)

for s in answer:
    print(*s)
