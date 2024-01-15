N=int(input()) # 3*2**K 3 6 12 24...
def star(n):
    if n==3:
        return ["  *  "," * * ","*****"]
    next=[]
    next2=[]
    for line in star(n//2):
        next.append((len(line)//2+1)*" "+line+(len(line)//2+1)*" ")
        next2.append(line+" "+line)
    return next+next2

for k in star(N):
    print(k)

