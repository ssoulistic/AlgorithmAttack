n=int(input())
divs=[]
for i in range(2,n+1):
    while n % i ==0:
        if n % i ==0:
            divs.append(i)
            n/=i
for num in divs:
    print(num)