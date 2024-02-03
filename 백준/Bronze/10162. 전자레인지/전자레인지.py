T=int(input())
A,B=divmod(T, 300)
B,C=divmod(B,60)
C,D=divmod(C,10)
if not D:
    print(A,B,C)
else:
    print(-1)