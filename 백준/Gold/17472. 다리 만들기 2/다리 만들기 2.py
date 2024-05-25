import sys
input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())

# 1. 섬 번호 정하기, 좌표 찾기.
island_map=[]
for _ in range(N):
    island_map.append(list(map(int,input().split())))

land_visited=[[-1 for _ in range(M)] for _ in range(N)]
lands={}
def find_land(row,col,land_number):
    if land_visited[row][col]!=-1:
        return False
    land_visited[row][col]=land_number
    lands[land_number]=[[row,col]]
    queue=deque()
    queue.append([row,col])
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    while queue:
        ri,ci=queue.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<N and 0<=nc<M and land_visited[nr][nc]==-1:
                if island_map[nr][nc]==1:
                    land_visited[nr][nc]=land_number
                    lands[land_number].append([nr,nc])
                    queue.append([nr,nc])
                else:
                    land_visited[nr][nc]=0
    return True
        
    
number=1
for r in range(N):
    for c in range(M):
        if island_map[r][c]==1:
            if find_land(r,c,number):
                number+=1
            

# 2. 각 섬에서 다른 섬으로 최단 거리 2칸이상
distance=[[1e8 for _ in range(len(lands))] for _ in range(len(lands))]

def near_island(island_num):
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    for r,c in lands[island_num]:
        for dr,dc in search:
            nr=r+dr
            nc=c+dc
            while 0<=nr<N and 0<=nc<M:
                
                if land_visited[nr][nc]>0: #만약 섬이라면
                    if land_visited[nr][nc]==island_num: 
                        break
                    else:
                        if abs(nr-r)+abs(nc-c)-1>=2:
                            distance[island_num-1][land_visited[nr][nc]-1]=min(distance[island_num-1][land_visited[nr][nc]-1],abs(r-nr)+abs(c-nc)-1)
                        break
                nr+=dr
                nc+=dc

for land_num in lands.keys():
    near_island(land_num)


# 3. MST를 통해 모든섬을 연결

queue_mst=[]
for i in range(len(lands)):
    for j in range(i+1,len(lands)):
        if distance[i][j]!=1e8:
            queue_mst.append([distance[i][j],i,j])
queue_mst.sort(reverse=True)

connected=[k for k in range(len(lands))]
def find(x):
    if connected[x]!=x:
        connected[x]=find(connected[x])
    return connected[x]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        connected[max(a,b)]=min(a,b)
        return True
    return False

answer=0
while queue_mst:
    dist,start,end=queue_mst.pop()
    if union(start,end):
        answer+=dist

Flag=True
for c in connected:
    if connected[c]==find(c)!=0:
        Flag=False
if Flag:
    print(answer)
else:
    print(-1)
