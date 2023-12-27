T=int(input())
answer=" "*(T-1)+"*"
for i in range(1,T):
    wrap=" "*(T-i-1)+"*"*(i*2+1)
    answer=wrap+("\n")+answer+("\n")+wrap
print(answer)