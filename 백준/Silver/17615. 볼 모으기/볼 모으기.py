import sys
input=sys.stdin.readline
N=int(input())
balls=input().strip()
left_end=balls[0]
right_end=balls[-1]

i=0
red=[]
blue=[]
R,B=0,0
while i<N:
    if balls[i]=="R":
        R+=1
        if B:
            blue.append(B)
            B=0
    elif balls[i]=="B":
        B+=1
        if R:
            red.append(R)
            R=0
    i+=1
if R:
    red.append(R)
if B:
    blue.append(B)

# RB
answer=N
if left_end=="R":
    answer=min(answer,sum(red[1:]))
else:
    answer=min(answer,sum(red))
if right_end=="B":
    answer=min(answer,sum(blue[:-1]))
else:
    answer=min(answer,sum(blue))

# BR
if left_end=="B":
    answer=min(answer,sum(blue[1:]))
else:
    answer=min(answer,sum(blue))
if right_end=="R":
    answer=min(answer,sum(red[:-1]))
else:
    answer=min(answer,sum(red))

print(answer)
    