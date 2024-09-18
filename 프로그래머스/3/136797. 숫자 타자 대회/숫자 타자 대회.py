import sys
sys.setrecursionlimit(10**9)
def solution(numbers):
    numbers=str(numbers)
    phone_key=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    floyd=[[float("inf") for _ in range(12)] for _ in range(12)]
    
    for r in range(4):
        for c in range(3):
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<4 and 0<=nc<3:
                    floyd[phone_key[r][c]-1][phone_key[nr][nc]-1]=2
            for dr2,dc2 in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                nr2=r+dr2
                nc2=c+dc2
                if 0<=nr2<4 and 0<=nc2<3:
                    floyd[phone_key[r][c]-1][phone_key[nr2][nc2]-1]=3
    for p in range(12):
        floyd[p][p]=1
    for k in range(12):
        for i in range(12):
            for j in range(12):
                floyd[i][j]=min(floyd[i][j],floyd[i][k]+floyd[k][j])

    dp=[[[-1 for _ in range(12)] for _ in range(12)]for _ in range(len(numbers)+1)]
    def dfs(left_hand,right_hand,idx):
        global answer
        if dp[idx][left_hand][right_hand]!=-1:
            return dp[idx][left_hand][right_hand]

        if idx==len(numbers):
            return 0 
        
        if numbers[idx] =="0":
            target=10
        else:
            target=int(numbers[idx])-1
        
        result=float('inf')
        if right_hand!=target:
            result=min(result,dfs(target,right_hand,idx+1)+floyd[left_hand][target])
        if left_hand!=target:
            result=min(result,dfs(left_hand,target,idx+1)+floyd[right_hand][target])
        dp[idx][left_hand][right_hand] = result
        return dp[idx][left_hand][right_hand]

    answer=dfs(3,5,0)
        
    return answer