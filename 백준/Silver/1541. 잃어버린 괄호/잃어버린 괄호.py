x=input().split('-')
answer=[]
for i in x:
    answer.append(sum(map(int,i.split("+"))))
print(eval("-".join(map(str,answer))))