def solve_pb(diffs,times,level):
    acc=times[0]
    for i in range(1,len(diffs)):
        acc+=max(0,diffs[i]-level)*(times[i-1]+times[i])+times[i]
    return acc

def solution(diffs, times, limit):
    start = 0
    end =  100001
    while start+1<end:
        mid=(start+end)//2
        if solve_pb(diffs,times,mid)<=limit:
            end=mid
        else:
            start=mid
    return end