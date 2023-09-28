while True:
    x=sorted(map(int,input().split()))
    a,b,c=x[0],x[1],x[2]
    if a==0:
        break
    if a**2+b**2==c**2:
        print("right")
    else:
        print("wrong")