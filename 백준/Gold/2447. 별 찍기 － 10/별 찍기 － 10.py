T=int(input())
def star(n):
    if n==3:
        return ["***","* *","***"]
    ex_star=["" for _ in range(n)]
    dstar=star(n//3)
    border=len(dstar)
    for j in range(n):
        if 2*border>j>=border:
            ex_star[j]=(dstar[j%border])+(" "*border)+(dstar[j%border])
        else:
            ex_star[j]+=(dstar[j%border])*3
    
    return ex_star
for shape in (star(T)):
    print(shape)