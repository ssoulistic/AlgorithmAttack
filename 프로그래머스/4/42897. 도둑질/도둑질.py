def solution(money):
    # 1. 0번을 골랐을때
    # 2. 1번을 골랐을때
    dp1=[[0,0] for _ in range(len(money))]
    dp1[0][0]=money[0]
    for i in range(len(money)-1):
        dp1[i+1][0]=dp1[i][1]+money[i+1]
        dp1[i+1][1]=max(dp1[i])
    
    dp2=[[0,0] for _ in range(len(money))]
    dp2[1][0]=money[1]
    for i in range(len(money)-1):
        dp2[i+1][0]=dp2[i][1]+money[i+1]
        dp2[i+1][1]=max(dp2[i])
    return max(max(dp1[-2]),max(dp2[-1]))