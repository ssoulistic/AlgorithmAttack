import sys
input=sys.stdin.readline
stack=[]
answer=0
a=""
for b in input().strip():
    if a=="(" and b==")": # 레이저
        answer+=len(stack)-1
        stack.pop()
    elif b=="(":
        stack.append("(")
    elif b==")":
        answer+=1
        stack.pop()
    a=b
        
    
print(answer)