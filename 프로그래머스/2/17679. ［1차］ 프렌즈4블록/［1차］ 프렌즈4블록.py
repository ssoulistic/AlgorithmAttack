def solution(m, n, board):
    # 높이 m 너비 n 좌표 기준 우측 상단..
    # 사라지는 함수 
    blocks=[]
    for i in range(m):
        temp=[]
        for j in range(n):
            temp.append(board[i][j])
        blocks.append(temp)
        
    def find(x,y):
        if blocks[y][x]==blocks[y+1][x]==blocks[y][x+1]==blocks[y+1][x+1]!=" ":
            return True
        return False
    
    def pang(x,y):
        blocks[y][x]=" "
        blocks[y+1][x]=" "
        blocks[y][x+1]=" "
        blocks[y+1][x+1]=" "

    def find2():
        answer=[]
        for i in range(n-1):
            for j in range(m-1):
                if find(i,j):
                    answer.append([i,j])
        return answer 
    
    # 떨어지는 함수
    def fall():
        falled=False
        c=0
        while c<n:
            temp=[]
            for l in range(m-1,-1,-1):
                if blocks[l][c]!=" ":
                    temp.append(blocks[l][c])
                    blocks[l][c]=" "
            if temp:
                for t in range(m-1,m-len(temp)-1,-1):
                    blocks[t][c]=temp[m-1-t]
            c+=1
        return falled
    
    while find2() or fall():
        
        for x1,y1 in find2():
            pang(x1,y1)
        fall()
    result=0
    for line in blocks:
        for l in line:
            if l ==" ":
                result+=1

    return result
