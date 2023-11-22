sudoku=[]
for _ in range(9):
    sudoku.append(list(map(int,input().split())))

def check_zero():
    zeroa=[]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] ==0:
                zeroa.append([j,i])
    return zeroa


def check_hor(coord):#가로줄 체크.
    avail=[1 for _ in range(9)]
    for num in sudoku[coord[1]]:    
        # 0이 아닌 구간 체크
        if num:
            if avail[num-1]:
                avail[num-1]-=1
            else:
                return False
    return avail

def check_ver(coord):
    avail=[1 for _ in range(9)]
    for line in sudoku:
        num=line[coord[0]]
        if num:
            if avail[num-1]:
                avail[num-1]-=1
            else:
                return False
    return avail

def check_square(coord):
    avail=[1 for _ in range(9)]
    part=[[0,1,2],[3,4,5],[6,7,8]]
    square=[part[coord[0] // 3], part[coord[1] // 3]]
    for j in square[0]:
        for i in square[1]:
            if sudoku[i][j]:
                if avail[sudoku[i][j]-1]:
                    avail[sudoku[i][j]-1]-=1
                else:
                    return False
    return avail

def sudo(idx):
    if idx==len(zeros):
        for ans in sudoku:
            print(*ans)
        exit(0)

    z=zeros[idx]
    d1=check_hor(z)
    d2=check_ver(z)
    d3=check_square(z)
    # 하나라도 False, 중복됨이 없을때.
    if d1 and d2 and d3:
        for i in range(9):
        # 가능한 수 가 있을경우
            if d1[i]==d2[i]==d3[i]==1:
                sudoku[z[1]][z[0]]=i+1
                sudo(idx+1)
                sudoku[z[1]][z[0]]=0
    else:
        return
zeros=check_zero()
sudo(0)
