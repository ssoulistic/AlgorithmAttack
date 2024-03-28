import sys
input=sys.stdin.readline

lotto=[]
def backtrack(l,num,arr):
    global lotto
    if len(lotto)==6:
        print(*lotto)
        return
    for i in range(l,num):
        if arr[i] not in lotto:
            lotto.append(arr[i])
            backtrack(i+1,num,arr)
            lotto.pop()
    return

while True:
    k,*S=list(map(int,input().split()))
    if k==0:
        break
    backtrack(0,k,S)
    print()


    