a,b=map(int,input().split())
x,y=a,b
while a % b:
    a,b=b,a%b
print(b)
print(x*y//b)