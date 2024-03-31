import sys
input=sys.stdin.readline
N=int(input())
eggs=[]
answer=0
for _ in range(N):
    S,W=map(int,input().split())
    eggs.append([S,W])

def stroke(idx):
    global answer
    state=list(map(lambda x: True if x[0]<=0 else False,eggs))
    if idx==N:
        broken=state.count(True)
        if broken>answer:   
            answer=broken
        return
    if all(state):
        answer=N
        return
    for i in range(N):
        if i!=idx:
            if eggs[i][0]>0 and eggs[idx][0]>0:
                eggs[i][0]-=eggs[idx][1]
                eggs[idx][0]-=eggs[i][1]
                stroke(idx+1)
                eggs[i][0]+=eggs[idx][1]
                eggs[idx][0]+=eggs[i][1]
            else:
                stroke(idx+1)
    return 
stroke(0)
print(answer)
