n=input()
l=[0 for _ in range(10)]
answer=''
for i in range(10):
    l[i]=n.count(str(i))
for idx,j in enumerate(l):
    answer=str(idx)*j+answer
print(answer)
    
    