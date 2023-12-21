import sys
N,M=map(int,sys.stdin.readline().split())
sheet=[]

for _ in range(N):
    sheet.append(list(map(int,sys.stdin.readline().split())))
visited=[[False for _ in range(M)] for _ in range(N)]
search=[[-1,0],[1,0],[0,-1],[0,1]]
maxi=0

def tetris(start,block):
    global maxi
    x1,y1=start
    visited[y1][x1]=True
    if len(block)==4:
        temp=0
        for b in block:
            xi,yi=b
            temp+=sheet[yi][xi]
        if maxi<temp:
            maxi=temp
        return
    for s in search:
        dx,dy=s
        if len(block)>=2:
            for bb in block:
                x2,y2=bb
                x3=x2+dx
                y3=y2+dy
                if 0<=x3<M and 0<=y3<N and not visited[y3][x3]:
                    visited[y3][x3]=True
                    block.append([x3,y3])
                    tetris([x3,y3],block)
                    block.pop()
                    visited[y3][x3]=False
        else:
                x2=x1+dx
                y2=y1+dy
                if 0<=x2<M and 0<=y2<N and not visited[y2][x2]:
                    visited[y2][x2]=True
                    block.append([x2,y2])
                    tetris([x2,y2],block)
                    block.pop()
                    visited[y2][x2]=False
    visited[y1][x1]=False
    return
for i in range(M):
    for j in range(N):
        tetris([i,j],[[i,j]])
print(maxi)