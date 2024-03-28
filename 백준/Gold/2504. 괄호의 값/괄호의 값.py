import sys
input=sys.stdin.readline
# 1. 올바른 괄호 찾기.
# 2. 올바른 괄호열 찾기.
# 3. 반복
# 4. 계산
exp=input().strip()
stack=[]
def stacking(word):
    dic={"(":0,"[":0}
    if word=="":
        return 1
    elif word=="()":
        return 2
    elif word=="[]":
        return 3
    elif word in ["(",")","[","]"]:
        print(0)
        exit(0)
    # 하나의 괄호 시작 => 2 또는 3 곱하기 시작
    if word[0]=="(":
        mul=2
        target=")"
        dic["("]+=1
    elif word[0]=="[":
        mul=3
        target="]"
        dic["["]+=1
    else:
        print(0)
        exit(0)
    k=1
    found=False
    while k<len(word):
        if word[k]=="[":
            dic["["]+=1
        elif word[k]=="]":
            dic["["]-=1
        elif word[k]=="(":
            dic["("]+=1
        elif word[k]==")":
            dic["("]-=1
        if dic[word[0]]==0 and word[k]==target:
            found=True
            break
        k+=1
    if found:
        if word[k+1:]:
            return mul*stacking(word[1:k])+stacking(word[k+1:])
        else:
            return mul*stacking(word[1:k])    
    else:
        print(0)
        exit(0)

print(stacking(exp))
    
    
    