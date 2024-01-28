from collections import deque
def solution(board):
    visited=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    def bfs(start):
        x,y=start
        visited[y][x]=1
        que=deque()
        que.append([x,y])
        search=[[-1,0],[1,0],[0,-1],[0,1]]
        while que:
            xi,yi=que.popleft()
            for dx,dy in search:
                nx=xi
                ny=yi
                while 0<=nx<len(board[0]) and 0<=ny<len(board) and board[ny][nx]!="D":
                    nx+=dx
                    ny+=dy
                nx-=dx
                ny-=dy
                if not visited[ny][nx]:
                    visited[ny][nx]=visited[yi][xi]+1
                    que.append([nx,ny])
                elif visited[ny][nx]>visited[yi][xi]+1:
                    visited[ny][nx]=visited[yi][xi]+1
                    que.append([nx,ny])
        return
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]=="G":
                e=[col,row]
            elif board[row][col]=="R":
                s=[col,row]
    bfs(s)
    answer=visited[e[1]][e[0]]
    if answer:
        return answer-1
    else:
        return -1