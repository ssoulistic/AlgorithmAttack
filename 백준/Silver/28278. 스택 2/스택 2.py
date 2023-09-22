import sys
N=int(sys.stdin.readline())
stack=[]
answer=[]
for _ in range(N):
    x = list(sys.stdin.readline().split())
    if x[0]=="1":
        stack.append(x[1])
    elif x[0]=="2":
        if stack:
            answer.append(stack.pop())
        else:
            answer.append("-1")
    elif x[0]=="3":
        answer.append(len(stack))
    elif x[0]=="4":
        if stack:
            answer.append("0")
        else:
            answer.append("1")
    elif x[0]=="5":
        if stack:
            answer.append(stack[-1])
        else:
            answer.append("-1")
for i in range(len(answer)):
    print(answer[i])
