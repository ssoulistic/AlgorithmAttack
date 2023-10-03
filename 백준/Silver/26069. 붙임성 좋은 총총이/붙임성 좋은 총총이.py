n=int(input())
dance=set()
dance.add("ChongChong")
for _ in range(n):
    partner=input().split()
    if partner[0] in dance:
        dance.add(partner[1])
    elif partner[1] in dance:
        dance.add(partner[0])
print(len(dance))