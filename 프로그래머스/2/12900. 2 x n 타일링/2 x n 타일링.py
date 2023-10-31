def solution(n):
    tile=[1 for _ in range(n+1)]
    tile[0]=1
    tile[1]=1
    tile[2]=2
    for i in range(1,n-1):
        tile[i+2]=(tile[i+1]+tile[i]) % 1000000007
    return tile[n]
