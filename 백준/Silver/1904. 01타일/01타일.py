n=int(input())
t=[1,2,3]

def tile(num):
    for i in range(2,num):
        t[(i)%3]=(t[(i-1)%3]+t[(i-2)%3])%15746
    return t[(num-1)%3]
print(tile(n))