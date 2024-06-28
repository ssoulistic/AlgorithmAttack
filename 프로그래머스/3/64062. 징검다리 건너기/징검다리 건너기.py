def solution(stones, k):
    stones.append(2*10**8+1)
    def movable(n):
        start=-1
        for i in range(len(stones)):
            if stones[i]-n>0:
                if (i-start)>k:
                    return False
                start=i
        return True
    l=1
    r=max(stones)
    while l<r:
        mid=(l+r)//2
        if not movable(mid):
            r=mid
        else:
            l=mid+1
    return r