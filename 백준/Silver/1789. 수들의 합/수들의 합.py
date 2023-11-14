T=int(input())
sum=0
for i in range(1,T+1):
    sum+=i
    if sum>T:
        print(i-1)
        break
if T==1:
    print(1)