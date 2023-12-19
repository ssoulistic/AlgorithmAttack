import sys
N,M=map(int,input().split()) #N세로 M 가로
for _ in range(N):
    up=list(sys.stdin.readline().strip())
    Q=list(sys.stdin.readline().strip())
    down=list(sys.stdin.readline().strip())
    for i in range(M):
        temp=""
        for j in range(8):
            if Q[8*i+j]!=".":
                temp+=Q[8*i+j]
        temp=temp.replace("=","==")
        if eval(temp):
            Q[8*i]="*"
            Q[8*i+len(temp)]="*"
            up[8*i+1:8*i+len(temp)]="*"*(len(temp)-1)
            down[8*i+1:8*i+len(temp)]="*"*(len(temp)-1)
        else:
            up[8*i+3]="/"
            Q[8*i+2]="/"
            down[8*i+1]="/"
    print("".join(up))
    print("".join(Q))
    print("".join(down))  