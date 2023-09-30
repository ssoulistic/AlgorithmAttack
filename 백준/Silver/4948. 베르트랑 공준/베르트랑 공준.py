test_list=[]
while True:
    x=int(input())
    if x!=0:
        test_list.append(x)
    else:
        break
end=max(test_list)*2
plist=[False]*2+[True]*end
for i in range(2,int(end**0.5)+1):
    for j in range(i*2,end+1,i):
        if plist[j]:
            plist[j]=False

for num in test_list:
    print(plist[num+1:num*2+1].count(True))