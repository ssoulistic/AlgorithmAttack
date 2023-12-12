import sys
T=int(sys.stdin.readline())
paper=[]
color={-1:0,0:0,1:0}
for _ in range(T):
    paper.append(list(map(int,sys.stdin.readline().split())))


def check_full(upleft,downright):
    x1,y1=upleft
    x2,y2=downright
    standard=paper[y1][x1]
    for xi in range(x1,x2+1):
        for yi in range(y1,y2+1):
            if paper[yi][xi]!=standard:
                return False
    return True

def conquer(upleft,downright):
    x1,y1=upleft
    x2,y2=downright
    gap=(x2-x1+1)//3
    if check_full([x1,y1],[x2,y2]):
        color[paper[y1][x1]]+=1
    else:
        for i in range(3):
            for j in range(3):
                conquer([x1+i*gap,y1+j*gap],[x1+(i+1)*gap-1,y1+(j+1)*gap-1])
conquer([0,0],[T-1,T-1])
for ans in color.values():
    print(ans)