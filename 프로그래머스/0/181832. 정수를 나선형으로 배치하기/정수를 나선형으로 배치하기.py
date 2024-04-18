def solution(n):
    dir_order=[[1,0],[0,1],[-1,0],[0,-1]]
    result=[[0 for _ in range(n)] for _ in range(n)]
    x,y,j=0,0,0
    add=dir_order[j]
    for i in range(n**2):
        #1. 위치 체크, O - 입력 X - 롤백후 방향 전환 한칸.
        if not ((n>x>=0) and (n>y>=0)) or result[y][x]!=0:
            x-=add[0]
            y-=add[1]
            j+=1
            add=dir_order[j % 4]
            x+=add[0]
            y+=add[1]
        result[y][x]=i+1
        x+=add[0]
        y+=add[1]
    return result