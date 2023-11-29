import sys
S=sys.stdin.readline().strip()
parsum=[[0 for _ in range(len(S)+1)] for _ in range(26)]
q=int(sys.stdin.readline().strip())

for s in range(len(S)):
    idx=ord(S[s])-97
    for k in range(26):
        if k==idx:
            parsum[k][s+1]=parsum[k][s]+1
        else:
            parsum[k][s+1]=parsum[k][s]

for _ in range(q):
    alpha,l,r=sys.stdin.readline().strip().split()
    idx_alpha=ord(alpha)-97
    l=int(l)
    r=int(r)
    print(parsum[idx_alpha][r+1]-parsum[idx_alpha][l])