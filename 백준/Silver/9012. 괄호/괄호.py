n = int(input())
def VPS(st):
    stack=[]
    for _ in range(n):
        for x in st:
            if x =="(":
                stack.append(x)
            else:
                if stack:
                    if stack[-1]=="(":
                        stack.pop()
                else:
                    return "NO"
    if stack:
        return "NO"
    else:
        return "YES"

for _ in range(n):
    print(VPS(input()))