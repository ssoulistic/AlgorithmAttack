def solution(grid):
    
    Ldir={6:7,8:1,2:3,4:5}
    Rdir={6:3,8:5,2:7,4:1}
    Sdir={2:5,4:7,6:1,8:3}
    convdir={1:6,2:5,3:8,4:7,5:2,6:1,7:4,8:3}
    drc={1:[-1,0],5:[1,0],3:[0,1],7:[0,-1]}
    answer = []
    visit_set=[]
    visited=[[[False for _ in range(8)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for d in range(4):
                
                vector=2*d+1
                acc=0
                while not visited[row][col][vector-1]:
                    visited[row][col][vector-1]=True
                    dr,dc=drc[vector]
                    nr=(row+dr) % len(grid)
                    nc=(col+dc) % len(grid[0])
                    next_core=grid[nr][nc]
                    if next_core=="S":
                        next_vector=Sdir[convdir[vector]]
                    elif next_core=="L":
                        next_vector=Ldir[convdir[vector]]
                    elif next_core=="R":
                        next_vector=Rdir[convdir[vector]]
                    visited[nr][nc][convdir[vector]-1]=True

                    acc+=1
                    vector=next_vector
                    row=nr
                    col=nc
                
                if acc>0:
                    visit_set.append(visited)
                    answer.append(acc)
    return sorted(answer)