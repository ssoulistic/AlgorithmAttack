import sys
input=sys.stdin.readline

# 1. 괄호가 있는지 확인 => 괄호가 없으면 => 곱,나눗셈,덧셈,뺄셈 형태로 진행
# 2. 괄호가 있다면 => 괄호 안의 것들을 재귀로 보낸 결과 값을 가져옴 => 다시한번 진행
expression=list(input().strip())

def post_order(exp):
    if exp==[]:
        return exp
    if "(" in exp:
        i=0
        start,end=-1,-1
        stack=[]
        while i<len(exp):
            if exp[i]=="(":
                stack.append(exp[i])
                if start==-1:
                    start=i
            elif exp[i]==")":
                stack.pop()
                if stack==[]:
                    end=i
            if start!=-1 and end!=-1:
                break
            i+=1
        mid=post_order(exp[start+1:end])
        return post_order(exp[:start]+mid+exp[end+1:])
    stack=[]
    j=0


    while j<len(exp):
        if stack and (stack[-1]=="*" or stack[-1]=="/"):
            cal=stack.pop()
            first=stack.pop()
            stack.append(first+exp[j]+cal)
        else:
            stack.append(exp[j])
        j+=1
    stack2=[]
    k=0
    while k<len(stack):
        if stack2 and (stack2[-1]=="+" or stack2[-1]=="-"):
            cal=stack2.pop()
            first=stack2.pop()
            stack2.append(first+stack[k]+cal)
        else:
            stack2.append(stack[k])
        k+=1

    return stack2

print(*post_order(expression))
