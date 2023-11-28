S=input()
parsum=[[0 for _ in range(len(S)+1)] for _ in range(26)]
q=int(input())
for s in range(len(S)):
    idx=ord(S[s])-97
    parsum[idx][s+1]=parsum[idx][s]+1
    for j in range(s+1,len(S)):
        parsum[idx][j+1]=parsum[idx][j]
for _ in range(q):
    alpha,l,r=input().split()
    idx_alpha=ord(alpha)-97
    l=int(l)
    r=int(r)
    print(parsum[idx_alpha][r+1]-parsum[idx_alpha][l])