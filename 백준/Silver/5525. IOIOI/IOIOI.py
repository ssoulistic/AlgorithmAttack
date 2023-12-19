N=int(input())
M=int(input())
S=input()
PN="I"+"OI"*N
answer=0
for i in range(M-(2*N+1)+1):
    if S[i:i+2*N+1]==PN:
        answer+=1
print(answer)