import sys
H=0
n=int(sys.stdin.readline().rstrip())
a=sys.stdin.readline().rstrip()
for i in range(n):
    H+=(ord(a[i])-96)*(31**i)
print(H % 1234567891)