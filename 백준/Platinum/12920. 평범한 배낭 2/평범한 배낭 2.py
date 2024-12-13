import sys
input=sys.stdin.readline
def main():
    N,M=map(int,input().split())
    mat=[]
    acc=0
    for _ in range(N):
        V,C,K=map(int,input().split())
        i=1
        while K>0:
            ix=min(i,K)
            mat.append([V*ix,C*ix])
            acc+=1
            i*=2
            K-=ix
    dp=[[0 for _ in range(M+1)] for _ in range(acc+1)]
    for idx in range(1,acc+1):
        V,C=mat[idx-1]
        for bag_weight in range(1,M+1):
            dp[idx][bag_weight]=dp[idx-1][bag_weight]   
            if bag_weight>=V and dp[idx][bag_weight]<dp[idx-1][bag_weight-V]+C:
                dp[idx][bag_weight]=dp[idx-1][bag_weight-V]+C
                
    print(dp[-1][-1])
main()
