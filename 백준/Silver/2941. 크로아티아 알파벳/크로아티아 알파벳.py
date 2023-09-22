characters=["c=","c-","d-","lj","nj","s=","z="]
x=input()
answer=len(x)
for i in characters:
    if i in x:
        answer-=x.count(i)
if "dz=" in x:
    answer-=x.count("dz=")
print(answer)