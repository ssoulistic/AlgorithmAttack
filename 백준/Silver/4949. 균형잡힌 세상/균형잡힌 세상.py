def PS(line):
    stack=[]
    for x in line:
        if x=="(" or x=="[":
            stack.append(x)
        elif x==")" or x=="]":
            if stack:
                if stack[-1] =="(" and x==")":
                    stack.pop()
                elif stack[-1]=="[" and x=="]":
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"
    if stack:
        return "no"
    else:
        return "yes"

while True:
    sentence=input()
    if sentence==".":
        break
    print(PS(sentence))