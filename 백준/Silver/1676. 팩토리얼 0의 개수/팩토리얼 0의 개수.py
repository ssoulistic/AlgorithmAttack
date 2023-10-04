n=int(input())
a=1
b=0
for i in range(1,n+1):
    a*=i
while a % 10==0:
    b+=1
    a//=10
print(b)
