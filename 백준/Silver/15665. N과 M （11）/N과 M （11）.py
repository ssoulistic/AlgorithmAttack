import sys
input=sys.stdin.readline
N,M=map(int,input().split())
seq=sorted(set(map(int,input().split())))
answer=[]
stack=[]
def backt():
    if len(stack)==M:
        print(*stack)
        return
    for i in range(len(seq)):
        stack.append(seq[i])
        backt()
        stack.pop()
    return

backt()
