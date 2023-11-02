T=input()
N=int(input())
house=['swi']
sus=[]
seen=set()
for _ in range(N):
    house.append(input())
M=int(input())
for _ in range(M):
    seen.add(input())

#목격담 체크
for h in house:
    if h not in seen:
        sus.append(h)


#집안에 있으면서 목격담이 없는 그룹 sus
if "dongho" in house:
    print("dongho")
elif len(sus)==1:
    print(*sus)
elif "bumin" in sus:
    print("bumin")
elif "cake" in sus:
    print("cake")
elif "lawyer" in sus:
    print("lawyer")
else:
    print(sorted(sus)[0])