import sys
input=sys.stdin.readline
N=int(input())
E=int(input())
song=0
people={}
answer=[]
for _ in range(E):
    K,*attend=map(int,input().split())
    if 1 in attend:
        song+=1
        for a in attend:
            if people.get(a):
                people[a].add(song)
            else:
                people[a]=set([song])
    else:
        share=set()
        for a in attend:
            if people.get(a):
                share=share.union(people[a])
        for a in attend:
            if people.get(a):
                people[a]=people[a].union(share)
            else:
                people[a]=set(share)
for k,v in people.items():
    if len(v)==song:
        answer.append(k)
for ans in sorted(answer):
    print(ans)
