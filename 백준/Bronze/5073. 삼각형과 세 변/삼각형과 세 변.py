while True:
    x,y,z=sorted(map(int,input().split()))
    if x==y==z==0:
        break
    if z>=x+y:
        print("Invalid")
    else:
        if x==y==z:
            print("Equilateral")
        elif x==y or y==z or x==z:
            print("Isosceles")
        elif x!=y and y!=z and x!=z:
            print("Scalene")