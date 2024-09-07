l=list(map(int,open(0)))
x,y,z=l[0],l[1],l[2]
if x==y==z==60:
    print("Equilateral")
elif x+y+z==180 and (x==y or y==z or x==z):
    print("Isosceles")
elif x+y+z==180 and (x!=y and y!=z and x!=z):
    print("Scalene")
else:
    print("Error")