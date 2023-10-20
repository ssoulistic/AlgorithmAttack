n=int(input())
wine=[]
for _ in range(n):
    wine.append(int(input()))
if n==1:
    print(wine[0])
elif n==2:
    print(wine[0]+wine[1])
else:
    drink_max=[0 for _ in range(len(wine))]
    drink_max[0]=wine[0]
    drink_max[1]=wine[1]+wine[0]
    drink_max[2]=max(drink_max[1],wine[0]+wine[2],wine[1]+wine[2])
    for i in range(3,n):
        drink_max[i]=max(drink_max[i-1],wine[i]+drink_max[i-2],wine[i]+wine[i-1]+drink_max[i-3])
    print(drink_max[n-1])
