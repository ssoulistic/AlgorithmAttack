text=input()
bomb=input()
stack=[]

for i in range(len(text)):
    stack.append(text[i])
    if len(stack)>=len(bomb):
        if "".join(stack[-len(bomb):])==bomb:
            for _ in range(len(bomb)):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")


