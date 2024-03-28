import sys
input=sys.stdin.readline
N,S=map(int,input().strip().split())
seq=list(map(int,input().strip().split()))
answer=0
stack=[]
def backtrack(k):
    global answer
    if len(stack)>N:
        return
    for i in range(k,N):
        stack.append(seq[i])
        if sum(stack)==S:
            answer+=1
        backtrack(i+1)
        stack.pop()
    return
backtrack(0)
print(answer)