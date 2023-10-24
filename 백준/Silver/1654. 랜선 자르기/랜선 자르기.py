K,N=map(int,input().split())
lan=[]
for _ in range(K):
    lan.append(int(input()))

# end 조건 : 이분탐색시 해당 값이 N개로 포괄 가능. +1한 상태에서는 불가한 최대 상태.
def end_condition(x):
    det=sum(map(lambda y:(y//x),lan))
    if N <= det:
        return True
    else:
        return False

def binary_search(start,end):
    mid=(start+end)//2
    if end_condition(end):
        return end
    elif end_condition(mid):
        if start==mid:
            return start
        return binary_search(mid,end)
    elif end_condition(start):
        return binary_search(start,mid)

print(binary_search(1,max(lan)))
