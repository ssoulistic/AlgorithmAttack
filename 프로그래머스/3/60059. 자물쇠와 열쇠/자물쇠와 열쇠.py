def solution(key, lock):
    # 자물쇠의 홈으로 서치 => 열쇠에서 완벽히 같은 모양 서치.(확장+회전 4회)
    # 90도 회전 함수 + 자기 사이즈-1 만큼 확장
    # 배열확장시 거진 60x60 => 3600 * 4 => 14400 byte 충분할듯?
    # 시간복잡도 n^2..
    pair=[[0 for _ in range(len(lock))]for _ in range(len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j]==0:
                pair[i][j]=1
            
    def rotate(arr):
        width=len(arr)
        result=[[0 for _ in range(width)] for _ in range(width)]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                result[i][j]=arr[len(arr)-1-j][i]
        return result
        
    def expand(arr,margin):
        width=2*margin+len(arr)
        result=[[0 for _ in range(width)] for _ in range(width)]
        
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                result[i+margin][j+margin]=arr[i][j]
        return result
    
    def match(key1,board):
        l1=len(key1)
        l2=len(board)
        for i in range(l2-l1+1):
            for j in range(l2-l1+1):
                x=check(key1,board,[i,j])
                if x:
                    return True
        return False
                
    def check(key1,board,coord):
        x,y=coord
        for k in range(len(key1)):
            for l in range(len(key1)):
                if key1[k][l]!=board[x+k][y+l]:
                    return False
        return True
    key=expand(key,len(lock)-1)
    for _ in range(4):
        key=rotate(key)
        if match(pair,key):
            return True
    return False