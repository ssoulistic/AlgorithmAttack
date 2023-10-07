n,k=map(int,input().split())
coin=[]
for _ in range(n):
    coin.append(int(input()))

count=0
for i in coin[::-1]:
    count+=k // i 
    k = k % i
print(count)