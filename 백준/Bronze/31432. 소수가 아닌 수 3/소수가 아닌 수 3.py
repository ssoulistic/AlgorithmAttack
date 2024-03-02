N=int(input())
pool=sorted(input().split())
if N==1 and pool[0]==0:
    print("YES")
    print(0)
else:
    print("YES")
    print(int(pool[-1]*3))