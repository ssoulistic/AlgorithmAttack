x=input()
answer=set()
for i in range(0,len(x)):
    for j in range(i+1,len(x)+1):
        answer.add(x[i:j])
print(len(answer))