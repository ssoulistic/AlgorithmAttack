def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
n,k=map(int,input().split())

print(int(factorial(n)/(factorial(k)*factorial(n-k))))