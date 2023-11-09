T=input()
stack=[]
answer=''
putin=False
# <가 나오면 >가 나올때까지 금지

for t in T:
    if putin:
        answer+=t
        if t==">":
            putin=False
    else:
        if t==" " or t=="<":
            while stack:
                answer+=stack.pop()
            answer+=t
        else:
            stack.append(t)
    if t=="<":
        putin=True
while stack:
    answer+=stack.pop()
    
print(answer)