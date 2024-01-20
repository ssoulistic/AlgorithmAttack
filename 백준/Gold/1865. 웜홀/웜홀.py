import sys
input= sys.stdin.readline
TC=int(input())

for _ in range(TC):
    N,M,W=map(int,input().split()) # N 지점 M 도로 W 웜홀
    command=[]
    
    for _ in range(M):
        S,E,T=map(int,input().split())
        command.append([S-1,E-1,T])
        command.append([E-1,S-1,T])
    for _ in range(W):
        S,E,T=map(int,input().split())
        command.append([S-1,E-1,-T])
    mapping=[1e10 for _ in range(N)]
    mapping[0]=0
    Flag=True
    count=0
    answer="NO"
    while Flag:
        Flag=False
        for start,end,time in command:
            if mapping[end]>mapping[start]+time:
                mapping[end]=mapping[start]+time
                Flag=True
        if Flag:
            count+=1
        if count>N:
            answer="YES"
            break
    print(answer)

