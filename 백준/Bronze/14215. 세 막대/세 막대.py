l=sorted(map(int,input().split()))
if l[0]+l[1]>l[2]:
    print(sum(l))
else:
    print(2*(l[0]+l[1])-1)
