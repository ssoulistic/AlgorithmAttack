n=int(input())
answer=[]
x=["0","1","2","3","4","5","6","7","8","9"]
doom=set()
doom.add("666")
while len(answer)==0:
    for j in list(doom):
        for i in x:
            doom.add(j+i)
            doom.add(i+j)
    if len(doom)>n:
        answer=sorted(set(map(int,doom)))
print(answer[n-1])