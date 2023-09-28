def gcd(a,b):
    if a % b==0:
        return b
    a,b= b, a % b
    return gcd(a,b)
a,b=map(int,input().split())
print(a*b//gcd(a,b))
