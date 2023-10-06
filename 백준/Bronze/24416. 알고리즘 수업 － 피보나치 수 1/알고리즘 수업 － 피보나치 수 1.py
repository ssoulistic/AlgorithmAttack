dp = [0 for _ in range(200)]
def fibo(n):
    if n <=1:
        return n
    else:
        if dp[n]>0:
            return dp[n]
        dp[n]=fibo(n-1)+fibo(n-2)
        return dp[n]

n=int(input())
print(fibo(n),n-2)