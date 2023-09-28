def gcd(a,b):
    if a % b ==0:
        return b 
    a,b=b,a%b
    return gcd(a,b)
def lcd(a,b):
    return a*b//gcd(a,b)

a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=lcd(a[1],b[1])
y=a[0]*(x//a[1])+b[0]*(x//b[1])
print(y//gcd(x,y),x//gcd(x,y))