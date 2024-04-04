import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def pre_to_post(start,end):
    if start==end:
        return [start]
    elif start>end:
        return []
    root=preorder[start]
    i=start
    while i<=end:
        if preorder[i]>root:
            break
        i+=1
    left=pre_to_post(start+1,i-1)
    right=pre_to_post(i,end)
    return left+right+[start]

preorder=[]
while True:
    x=input().strip()
    if x=='':
        break
    preorder.append(int(x))
for p in pre_to_post(0,len(preorder)-1):
    # print(p)
    print(preorder[p])
