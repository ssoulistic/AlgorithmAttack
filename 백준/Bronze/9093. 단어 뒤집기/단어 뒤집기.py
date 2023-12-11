T=int(input())
for _ in range(T):
    words=input().split()
    stack=[]
    for word in words:
        for w in word:
            stack.append(w)
        while stack:
            print(stack.pop(),end="")
        print(" ",end="")
    print()