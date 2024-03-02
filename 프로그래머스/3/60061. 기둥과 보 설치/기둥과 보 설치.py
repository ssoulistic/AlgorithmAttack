def solution(n, build_frame):
    wall=[[[0,0] for _ in range(n+1)] for _ in range(n+1)]
    
    # 설치 가능한지 체크하는 함수(존재가능한지) -> 해당 위치.
    def exist(coord,comp):
        r,c=coord
        if comp==0: # 기둥
            # 바닥이거나
            if r==len(wall)-1:
                return True
            # 아래 기둥 있거나
            elif r+1<len(wall) and wall[r+1][c][0]:
                return True
            # 보가 어느쪽이던 있던가
            elif (c-1>=0 and wall[r][c-1][1]) or wall[r][c][1]:
                return True
        elif comp==1: # 보
            # 한쪽에 기둥위에 있거나 양쪽이 보
            if (r+1<len(wall) and wall[r+1][c][0]) or (r+1<len(wall) and c+1<len(wall[0]) and wall[r+1][c+1][0]) or ((c-1>=0 and wall[r][c-1][1]) and (c+1<len(wall[0]) and wall[r][c+1][1])):
                return True
        return False
    # 삭제 가능한지 체크 하는 함수 -> 삭제시 주변이 존재가능한지 체크. 불가능하면 원상복귀
    def delete(coord,comp):
        # 삭제되면 어떻게 되는지
        r,c=coord
        # 기둥 - 바로위 기둥, 위쪽의 보(양쪽)
        # 존재하면 따져줘야함..
        if comp==0:
            temp=True
            wall[r][c][comp]=0
            for x,y,a in [[r-1,c,0],[r-1,c-1,1],[r-1,c,1]]:
                if 0<=x<len(wall) and 0<=y<len(wall) and wall[x][y][a]:
                        if not exist([x,y],a):
                            temp=False
                            break
            if temp:
                return True
            else:
                wall[r][c][comp]=1
                return False
        # 보 - 양쪽의 보, 양쪽의 기둥    
        elif comp==1:
            temp=True
            wall[r][c][comp]=0
            for x,y,a in [[r,c-1,1],[r,c+1,1],[r,c,0],[r,c+1,0]]:
                if 0<=x<len(wall) and 0<=y<len(wall) and wall[x][y][a]:
                        if not exist([x,y],a):
                            temp=False
                            break
            if temp:
                return True
            else:
                wall[r][c][comp]=1
                return False
    answer = []
    for x,y,a,b in build_frame:
        # a 0 기둥 1 보 b 0 삭제 1 설치
        r=len(wall)-y-1
        c=x
        # print([x,y],[r,c],len(wall))
        if b==1: #설치
            if (exist([r,c],a)):
                wall[r][c][a]=1
        elif b==0: #삭제
            if delete([r,c],a):
                wall[r][c][a]=0
                
            
    for i in range(len(wall)):
        for j in range(len(wall)):
            r=len(wall)-i-1
            c=j
            if wall[r][c][0]:
                answer.append([j,i,0])
            if wall[r][c][1]:
                answer.append([j,i,1])
    return sorted(answer)