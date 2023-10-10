T=int(input())
time=list(map(int,input().split()))
ATM=zip(list(i for i in range(len(time))),time)
ATM=sorted(ATM,key=lambda x: x[1])
acc_time=[0 for _ in range(len(ATM))]
acc_time[0]=ATM[0][1]
for j in range(len(ATM)-1):
    acc_time[j+1]=acc_time[j]+ATM[j+1][1]
print(sum(acc_time))
