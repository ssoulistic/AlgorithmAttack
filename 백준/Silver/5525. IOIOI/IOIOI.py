N=int(input()) # N PN을 생성.I+OI*N회
M=int(input()) # S의 길이
S=input() # S
P="I"+"OI"*N
IOI=0
answer=0
idx=0
while idx<M-2:
    if S[idx]=="I" and S[idx+1]=="O" and S[idx+2]=="I":
        IOI+=1
        if IOI==N:
            IOI-=1
            answer+=1
        idx+=1
    else:
        IOI=0
    idx+=1
print(answer)