S=input()
counter={"0":0,"1":0}
mem=S[0]
counter[mem]+=1
i=0
while i<len(S):
    if S[i]!=mem:
        counter[S[i]]+=1
        mem=S[i]
    i+=1
print(min(counter.values()))

