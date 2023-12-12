N,r,c=map(int,input().split())
answer=0

def Z_repeat(row,col,z):
    global answer
    if z==0:
        return
    row_dim,row_next=divmod(row,z)
    col_dim,col_next=divmod(col,z)
    answer+=row_dim*2*(z**2)+col_dim*(z**2)
    Z_repeat(row_next,col_next,z//2)
Z_repeat(r,c,2**N)
print(answer)