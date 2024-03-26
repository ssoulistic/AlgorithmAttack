import sys
input=sys.stdin.readline
from itertools import combinations
N,C=map(int,input().split())
mat=list(map(int,input().split()))
mid=len(mat)//2
answer=0
A,B=mat[:mid],mat[mid:]
A_acc=[]
B_acc=[]

for i in range(len(A)+1):
    for A_comb in combinations(A,i):
        A_acc.append(sum(A_comb))

for j in range(len(B)+1):
    for B_comb in combinations(B,j):
        B_acc.append(sum(B_comb))
B_acc.sort()

for k in A_acc:
    if C-k>0:
        start=0
        end=len(B_acc)
        while start<end:
            middle=(start+end)//2
            if B_acc[middle]>C-k:
                end=middle
            elif B_acc[middle]<=C-k:
                start=middle+1
        answer+=end
    elif C-k==0:
        answer+=1

print(answer)