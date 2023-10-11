T=int(input())
fdp=[[0,0,0] for _ in range(41)]
fdp[0]=[1,0,0]
fdp[1]=[0,1,1]
def fib(n):
    if n==0:       
        return fdp[0]
    elif n==1:
        return fdp[1]
    else:
        for j in range(3):
            for i in range(n-1):
                fdp[i+2][j]=fdp[i+1][j]+fdp[i][j]
        return fdp[n]

for _ in range(T):
    x=int(input())
    print(*fib(x)[:2])
