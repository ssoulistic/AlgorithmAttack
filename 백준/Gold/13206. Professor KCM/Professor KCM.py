import sys
input=sys.stdin.readline
T=int(input())

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

for _ in range(T):
    N=int(input())
    seq=sorted(map(int,input().split()))
    for i in range(N-1):
        seq[i],seq[i+1]=gcd(seq[i],seq[i+1]),lcm(seq[i],seq[i+1])
    print(seq[-1]%1000000007 )
      
    