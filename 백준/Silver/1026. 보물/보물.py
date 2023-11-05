T=int(input())
N1=list(map(int,input().split()))
N2=list(map(int,input().split()))
N1.sort(reverse=True)
N2.sort()
answer=0
for i in range(T):
    answer+=N1[i]*N2[i]
print(answer)