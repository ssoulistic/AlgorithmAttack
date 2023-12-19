import sys
T=int(sys.stdin.readline().strip())
for _ in range(T):
    M,N,x,y=map(int,sys.stdin.readline().strip().split())
    answer=""
    for i in range(N):
        if ((M*i+x)-y) % N==0:
            answer=M*i+x
            break
    if answer:
        print(answer)
    else:
        print(-1)