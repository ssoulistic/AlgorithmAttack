T=int(input())
A=list(map(int,input().split()))
B=list()
dic={}
#각 갯수 체크.
for i in A:
    if dic.get(i):
        dic[i]+=1
    else:
        dic[i]=1
p=[]
# 탐색 시작
answer=[-1 for _ in range(T)]
for j in range(len(A)-1):
    p.append((j,dic[A[j]]))
    while p and p[-1][1]<dic[A[j+1]]:
        answer[p.pop()[0]]=A[j+1]
    
print(*answer)
