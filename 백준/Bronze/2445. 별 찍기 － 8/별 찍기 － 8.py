T=int(input())
answer="*"*T*2
for i in range(1,T):
    wrap="*"*(T-i)+" "*i*2+"*"*(T-i)
    answer=wrap+("\n")+answer+("\n")+wrap
print(answer)