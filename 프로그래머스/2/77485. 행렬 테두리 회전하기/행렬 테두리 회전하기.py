def solution(rows, columns, queries):
    matrix = [[i+1+j*columns for i in range(columns) ] for j in range(rows)]
    answer=[]
    def rotate(srow,scol,erow,ecol):
        search=[[1,0],[0,1],[-1,0],[0,-1]]
        mini=rows*columns
        # 하나식 next 형태로 넘기기
        before=matrix[srow-1][scol-1]
        ny,nx=srow,scol
        for dx,dy in search:
            xi=nx+dx
            yi=ny+dy
            while scol<=xi<=ecol and srow<=yi<=erow:
                if before<mini:
                    mini=before
                save=matrix[yi-1][xi-1]
                if before:
                    matrix[yi-1][xi-1]=before
                before=save
                xi+=dx
                yi+=dy
            xi-=dx
            yi-=dy
            nx=xi
            ny=yi
        answer.append(mini)
    for q in queries:
        sr,sc,er,ec=q
        rotate(sr,sc,er,ec)
    
    return answer