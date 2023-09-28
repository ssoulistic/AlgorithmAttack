n=int(input())
quest=input().split()
counting={}
for key in quest:
    if counting.get(key):
        counting[key]+=1
    else:
        counting[key]=1
m=int(input())
for r in (input().split()):
    if counting.get(r):
        print(counting[r],end=" ")
    else:
        print(0,end=' ')