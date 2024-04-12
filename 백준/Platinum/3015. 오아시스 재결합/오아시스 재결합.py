import sys
input=sys.stdin.readline
N=int(input())
stack=[]
count=0
for _ in range(N):
    x=int(input())
    # 작은것이 들어올때
   
    if stack and stack[-1][0]>x:
        count+=1
        stack.append([x,1])
    # 같은것이 들어올때
    elif stack and stack[-1][0]==x:
        count+=stack[-1][1]
        stack[-1][1]+=1
        # 더 큰 것이 존재하면
        if len(stack)>=2:
            count+=1
        
    # 큰 -> 앞에 자기보다 작은사람들은 뒷사람을 어차피 못봄.
    elif stack and stack[-1][0]<x:
        while stack and stack[-1][0]<x:
            height,num=stack.pop()
            count+=num
        # 자기가 가장 크면
        if not stack:
            stack.append([x,1])
        # 자신과 같은게 있으면
        elif stack and stack[-1][0]==x:
            count+=stack[-1][1]
            stack[-1][1]+=1
            if len(stack)>=2:
                count+=1
        # 자신이 가장 크진 않으면
        elif stack and stack[-1][0]>x:
            count+=1
            stack.append([x,1])

    # 초기
    elif not stack:
        stack.append([x,1])
print(count)