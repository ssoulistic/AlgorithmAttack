import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    candi=[]
    answer=[]
    for _ in range(N):
        candi.append(list(map(int,input().split())))
    candi.sort()
    answer=N
    # 앞의 사람들보다 모두 등수가 높으면 생존.
    best=candi[0][1]
    for i in range(1,len(candi)): # 비교군 2등부터.
        if best<candi[i][1]: # 앞사람 뒷사람. 
            answer-=1
        else:
            best=candi[i][1]
    print(answer)