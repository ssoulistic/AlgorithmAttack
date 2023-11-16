# 하노이 => n짜리 이동(3) => n-1짜리 이동(1,2) + 1 3 + n-1짜리 이동(2,3)
move=[]
def hanoi(n,depart,dest):
    if n==1:
        move.append(f'{depart} {dest}')
    else:
        medium=6-depart-dest
        hanoi(n-1,depart,medium)
        move.append(f'{depart} {dest}')
        hanoi(n-1,medium,dest)    
    return move
T=int(input())
answer=hanoi(T,1,3)
print(len(answer))
for i in answer:
    print(i)