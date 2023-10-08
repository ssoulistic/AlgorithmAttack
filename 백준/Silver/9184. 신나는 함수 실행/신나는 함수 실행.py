import sys
dp=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(x,y,z):
    if x<=0 or y<=0 or z<=0:
        return 1
    elif x>20 or y >20 or z>20:
        return w(20,20,20)
    elif x<y<z:
        if dp[x][y][z]:
            return dp[x][y][z]
        else:
            dp[x][y][z]=w(x,y,z-1)+w(x,y-1,z-1)-w(x,y-1,z)
            return dp[x][y][z]
    else:
        if dp[x][y][z]:
            return dp[x][y][z]
        else:
            dp[x][y][z]=w(x-1,y,z)+w(x-1,y-1,z)+w(x-1,y,z-1)-w(x-1,y-1,z-1)
            return dp[x][y][z]

while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')