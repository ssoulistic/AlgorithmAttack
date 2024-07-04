import sys
input= sys.stdin.readline
N=int(input())
n=int(N**(0.5))
if N<=4:
    print(4)
elif n*n>=N:
    print(4*(n-1))
elif n*(n+1)>=N:
    print(2*(2*n-1))
elif (n+1)**2>=N:
    print(4*n)
    