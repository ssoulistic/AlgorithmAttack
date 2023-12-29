A,B=map(int,input().split())
answer=0
def maker(n,count):
    global answer
    if n==B:
        answer=count
        return count
    elif n>B:
        return
    else:
        maker(2*n,count+1)
        maker(int(str(n)+"1"),count+1)
maker(A,0)
if answer:
    print(answer+1)
else:
    print(-1)