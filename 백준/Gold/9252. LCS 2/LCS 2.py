import sys
input=sys.stdin.readline

A=input().strip()
B=input().strip()

lcs=[[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for j in range(len(B)):
    for i in range(len(A)):
        if A[i]==B[j]:
            lcs[j+1][i+1]=lcs[j][i]+1
        else:
            lcs[j+1][i+1]=max(lcs[j+1][i],lcs[j][i+1])
answer=lcs[len(B)][len(A)]

def backt():
    r,c=len(B),len(A)
    word=""
    while r>=0 and c>=0:
        if lcs[r][c]==lcs[r-1][c]:
            r-=1
        elif lcs[r][c]==lcs[r][c-1]:
            c-=1
        elif lcs[r-1][c-1]+1==lcs[r][c]:
            word+=B[r-1]
            r-=1
            c-=1
        elif lcs[r][c]==0:
            break
    return word
if answer:
    print(answer)
    print(backt()[::-1])
else:
    print(answer)
