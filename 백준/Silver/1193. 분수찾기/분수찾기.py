n=int(input())
m,acc=0,0
while n>acc:
    m+=1
    acc+=m
x=(n-acc-1) % m
if m % 2==0:
    print(f'{x+1}/{m-x}')
else:
    print(f'{m-x}/{x+1}')