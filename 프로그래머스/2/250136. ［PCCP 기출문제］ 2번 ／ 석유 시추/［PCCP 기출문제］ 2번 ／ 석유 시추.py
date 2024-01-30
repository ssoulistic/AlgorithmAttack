from collections import deque
def solution(land):

    def detect(coord):
        x,y=coord
        if land[y][x]!=1:
            return
        que=deque()
        que.append([x,y])
        search=[[-1,0],[1,0],[0,-1],[0,1]]
        land[y][x]=2
        area=1
        situ=set()
        situ.add(x)
        while que:
            xi,yi=que.popleft()
            for dx,dy in search:
                nx=xi+dx
                ny=yi+dy
                if 0<=nx<len(land[0]) and 0<=ny<len(land) and land[ny][nx]==1:
                    area+=1
                    land[ny][nx]=2
                    que.append([nx,ny])
                    situ.add(nx)
        for s in situ:
            oil[s]+=area
        return 
    
    oil=[0 for _ in range(len(land[0]))]
    for col in range(len(land[0])):
        for row in range(len(land)):
            detect([col,row])
    return max(oil)