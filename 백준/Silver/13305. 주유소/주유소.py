T=int(input())
price=list(map(int,input().split()))
city=list(map(int,input().split()))

# 뒤와 쭉 비교 => 작아질때까지 => 거기까지의 거리
money=0
loc=0
while loc<len(city)-1:
    if city[loc]<city[loc+1]:
        city[loc+1]=city[loc]
    loc+=1
for i in range(len(city)-1):
    money+=city[i]*price[i]
print(money)


