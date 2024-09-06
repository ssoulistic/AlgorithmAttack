def solution(sticker):
    if len(sticker)==1:
        return sticker[0]
    dp1=[[0,0] for _ in range(len(sticker))]
    dp1[0][0]+=sticker[0]
    for i in range(len(sticker)-1):
        dp1[i+1]=[dp1[i][1]+sticker[i+1],max(dp1[i])]
    dp1[-1][0]=dp1[-1][1]
    
    dp2=[[0,0] for _ in range(len(sticker))]
    for i in range(len(sticker)-1):
        dp2[i+1]=[dp2[i][1]+sticker[i+1],max(dp2[i])]
    
    return max(max(dp1[-1]),max(dp2[-1]))