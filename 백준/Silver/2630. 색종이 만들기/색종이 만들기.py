import sys
N=int(sys.stdin.readline())
paper=[]
blue=0
white=0
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

def cutter(square):
    global blue
    global white
    stand=square[0][0]
    half=len(square)//2
    part1,part2,part3,part4=[],[],[],[]
    
    for p in range(len(square)):
        if p<half:
            part1.append(square[p][:half])
            part2.append(square[p][half:])
        else:
            part3.append(square[p][:half])
            part4.append(square[p][half:])

    
    for i in range(len(square)):
        for j in range(len(square)):
            if stand!=square[i][j]:
                cutter(part1)
                cutter(part2)
                cutter(part3)
                cutter(part4)
                return
    if stand==1:
        blue+=1
    else:
        white+=1
cutter(paper)
print(white)
print(blue)    