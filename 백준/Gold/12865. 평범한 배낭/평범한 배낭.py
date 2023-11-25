N,K=map(int,input().split())
bags=[[0 for _ in range(K+1)] for _ in range(N+1)]
# 가로축 : 가방에 든 무게.
# 세로축 : N번째 물건
for i in range(1,N+1):
    W,V=map(int,input().split())
    for j in range(K+1):
        # 가방에서 무게만큼 뺀 것 + 물건 vs 기존
        if j-W>=0:
            bags[i][j]=max(bags[i-1][j],bags[i-1][j-W]+V)
        
        # 무게 변화해도 달라지는게 없는 구간
        else:
            bags[i][j]=bags[i-1][j]
print(bags[N][K])