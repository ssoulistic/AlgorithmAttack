def solution(arr):
    answer = [0,0]
    def quadtree(array,start,size):
        x1,y1=start
        standard=array[y1][x1]
        for i in range(y1,y1+size):
            for j in range(x1,x1+size):
                if array[i][j]!=standard:
                    size//=2
                    quadtree(array,[x1,y1],size)
                    quadtree(array,[x1+size,y1],size)
                    quadtree(array,[x1,y1+size],size)
                    quadtree(array,[x1+size,y1+size],size)                
                    return
        answer[standard]+=1
    quadtree(arr,[0,0],len(arr))
    return answer