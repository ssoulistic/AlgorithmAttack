import sys
n=int(sys.stdin.readline())

test_list=[]
for _ in range(n):
    test_list.append(int(sys.stdin.readline()))

prime_numbers=[False]*2+[True]*max(test_list)
for i in range(2,int(max(test_list)**(1/2))+1):
    for j in range(i+i,max(test_list),i):
        if prime_numbers[j]==True:
            prime_numbers[j]=False

for x in test_list:
    answer=0
    for k in range(2,x//2+1):
        if prime_numbers[k] and prime_numbers[x-k]:
            answer+=1
    print(answer)
