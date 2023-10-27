def solution(board):
    #1. 선후공 숫자 체크
    xb="".join(board)
    o=xb.count("O")
    x=xb.count("X")
    if o-x<0 or o-x>=2:
        return 0
    #2. 빙고 조건 일치 체크
    bingo_o=0
    bingo_x=0
    bingo_req=["012","345","678","036","147","258","048","246"]
    for bingo in bingo_req:
        if xb[int(bingo[0])]==xb[int(bingo[1])]==xb[int(bingo[2])]:
            if xb[int(bingo[0])]=="O":
                bingo_o+=1
            elif xb[int(bingo[0])]=="X":
                bingo_x+=1
                
    #선공 승 또는 게임중/끝
    if bingo_o>=1 and bingo_x==0:
        if o-x==1:
            return 1
        else:
            return 0
    elif bingo_x>=1 and bingo_o==0:
        if o-x==0:
            return 1
        else:
            return 0
    elif bingo_o==0 and bingo_x==0:
        return 1
    else:
        return 0
        
    
        