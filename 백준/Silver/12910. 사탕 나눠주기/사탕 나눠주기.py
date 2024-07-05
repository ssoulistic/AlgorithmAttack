import sys
input=sys.stdin.readline
N=int(input())
candies=list(map(int,input().split()))
dic={}
for i in candies:
    if dic.get(i):
        dic[i]+=1
    else:
        dic[i]=1

j=1
acc=1
answer=0
while j<=N:
    if dic.get(j):
        acc*=dic[j]
    else:
        break
    answer+=acc
    j+=1
print(answer)
