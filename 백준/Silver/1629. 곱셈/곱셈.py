A,B,C=map(int,input().split())
def divnum(n,repeat):
    number=1
    count=0
    while count<repeat:
        number*=n
        count+=1
        over,left=divmod(number,C)
        if over:
            skip,left2 =divmod(repeat,count)
            return (divnum(left,skip)*(n**left2)) % C
    return left
print(divnum(A,B))