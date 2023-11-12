T=int(input())
fb=[1 for _ in range(T)]
for i in range(T-2):
    fb[i+2]=fb[i+1]+fb[i]
print(fb[T-1])
