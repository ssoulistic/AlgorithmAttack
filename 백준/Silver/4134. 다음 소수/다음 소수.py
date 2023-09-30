n=int(input())

def isPrime(num):
    if num in [0,1]:
        return False
    for i in range(2,int(num**(1/2)+1)):
        if num % i ==0:
            return False
    return True
for _ in range(n):
    x=int(input())
    Flag=True
    while Flag:
        if isPrime(x):
            print(x)
            Flag=False
        x+=1