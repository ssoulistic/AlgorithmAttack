from itertools import combinations
def solution(line):
    # 평행x시 => 조합 => 교점 => 정렬하여 기준으로 그림 그리기
    cross=[]
    xs=[]
    ys=[]
    for a,b in combinations(line,2):
        A,B,E=a
        C,D,F=b
        if A*D-B*C!=0:
            x=(B*F-E*D)/(A*D-B*C)
            y=(E*C-A*F)/(A*D-B*C)
            if x % 1 == 0 and y % 1==0 and [x,y] not in cross:
                cross.append([int(x),int(y)])
                xs.append(int(x))
                ys.append(int(y))
    
    # 상대좌표 -> 가장 좌상단
    xlen=max(xs)-min(xs)+1
    stcol=min(xs)
    ylen=max(ys)-min(ys)+1
    strow=max(ys)
    answer=[["." for _ in range(xlen)] for _ in range(ylen)]
    for c,r in cross:
        answer[strow-r][c-stcol]="*"
    answer=list(map(lambda x: "".join(x),answer))
    return answer