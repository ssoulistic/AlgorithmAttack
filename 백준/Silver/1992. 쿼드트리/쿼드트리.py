N=int(input().strip())
movie=[[] for _ in range(N)]
answer=""

for i in range(N):
    line=input().strip()
    for l in line:
        movie[i].append(int(l))


def check(screen):
    standard=screen[0][0]
    for a in range(len(screen)):
        for b in range(len(screen)):
            if screen[a][b]!=standard:
                return -1
    return standard

def zipper(scene):
    global answer
    d=check(scene)
    if d==-1:
        answer+="("
        part1,part2,part3,part4=[],[],[],[]
        half=len(scene)//2
        # 4등분하여 보기
        for p in range(len(scene)):
            if p<half:
                part1.append(scene[p][:half])
                part2.append(scene[p][half:])
            else:
                part3.append(scene[p][:half])
                part4.append(scene[p][half:])
        for q in [part1,part2,part3,part4]:
            d=check(q)
            if d==-1:
                zipper(q)
                answer+=")"
            else:
                answer+=str(d)
    else:
        answer+=str(d)

zipper(movie)
if answer[0]=="(":
    print(answer+")")
else:
    print(answer)
