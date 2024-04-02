import sys
input=sys.stdin.readline
N=int(input())
eggs=[]
answer=0
for _ in range(N):
    S,W=map(int,input().split())
    eggs.append([S,W])

def stroke(idx,cnt):
    global answer
    if idx==N:
        if cnt>answer:   
            answer=cnt
        return
    
    for i in range(N):
        if i!=idx:
            if eggs[i][0]>0 and eggs[idx][0]>0:
                eggs[i][0]-=eggs[idx][1]
                eggs[idx][0]-=eggs[i][1]
                stroke(idx+1,cnt+int(eggs[i][0]<=0)+int(eggs[idx][0]<=0))
                eggs[i][0]+=eggs[idx][1]
                eggs[idx][0]+=eggs[i][1]
            else:
                stroke(idx+1,cnt)
    return 
stroke(0,0)
print(answer)
