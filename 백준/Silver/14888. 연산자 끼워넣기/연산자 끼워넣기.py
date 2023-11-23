import sys
N=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
#중복x인 순열 조합 구하기.
tool=list(map(int,sys.stdin.readline().split()))
sign=["+","-","*","/"]
maxi=-1000000000
mini=1000000000
tt=[]
def calc(a,b,com):
    if com=="+":
        return a+b
    elif com =="-":
        return a-b
    elif com =="*":
        return a*b
    elif com =="/":
        if a<0 and b>0:
            return-((-a)//b)
        else:
            return a//b


def fs(n):
    global mini
    global maxi
    if n==len(nums)-1:
        result=nums[0]
        for i in range(1,len(nums)):
            result=calc(result,nums[i],tt[i-1])
        if mini>result:
            mini=result
        if maxi<result:
            maxi=result
        return
    for j in range(4): # 한가지씩 넣기..
        if tool[j]>0:
            tool[j]-=1
            tt.append(sign[j])
            fs(n+1)
            tool[j]+=1
            tt.pop()
    
fs(0)
print(maxi)
print(mini)