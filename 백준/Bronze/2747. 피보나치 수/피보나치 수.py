T=int(input())
fb=[0 for _ in range(T+1)]
fb[1]=1
for i in range(T-1):
    fb[i+2]=fb[i+1]+fb[i]
print(fb[T])
    
    