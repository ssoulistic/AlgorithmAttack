n=int(input())
stair_score=[]
for _ in range(n):
    stair_score.append(int(input()))
ss=[[0,0]for _ in range(n)]

if n==1:
    print(stair_score[0])
elif n==2:
    print(stair_score[0]+stair_score[1])
else:
    ss[0][0]=stair_score[0]
    ss[1][0]=stair_score[0]+stair_score[1]
    ss[1][1]=stair_score[1]
    for i in range(2,n):
        ss[i][0]=ss[i-1][1]+stair_score[i]
        ss[i][1]=max(ss[i-2][0],ss[i-2][1])+stair_score[i]
    print(max(ss[n-1]))