n=int(input())
stack=[1]
i=1
answer=['+']
for _ in range(n):
    x=int(input())
    while True:
        if stack and stack[-1]==x:
            answer.append("-")
            stack.pop()
            break
        elif i>=n:
            break
        else:
            i+=1
            answer.append("+")
            stack.append(i)
if stack:
    print("NO")
else:
    for j in answer:
        print(j)