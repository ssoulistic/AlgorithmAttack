x=input()
count=0
for j in range(1,int(x)+1):
    diff=set()
    num=str(j)
    for i in range(len(num)-1):
        diff.add(int(num[i])-int(num[i+1]))
    if len(diff)==0 or len(diff)==1:
        count+=1
print(count)