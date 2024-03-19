import sys
input=sys.stdin.readline
pre1,suf1=input().strip().split("*")
pre2,suf2=input().strip().split("*")
answer="A"*101
# 1. 조합 => 겹O 겹X
# 2. 조건 체크
def check(word):
    if (word.startswith(pre1) and word.endswith(suf1) and len(word)>=len(pre1+suf1)) and (word.startswith(pre2) and word.endswith(suf2) and len(word)>=len(pre2+suf2)):
        return True
    return False

def shrink(front,back):
    for j in range(min(len(front),len(back))+1):
        # print(back[:j],front[len(front)-j:])
        if back[:j]==front[len(front)-j:]:
            longest=back[:j]
    return (front+back.replace(longest,"",1))

def combo(pre,suf):
    global answer
    if check(pre+suf):
        if len(answer)>=len(pre+suf):
            answer=pre+suf
    new=shrink(pre,suf)
    if check(new):
        if len(answer)>=len(new):
            answer=new

combo(pre1,suf1)
combo(pre1,suf2)
combo(pre2,suf1)
combo(pre2,suf2)
if answer=="A"*101:
    answer=-1
elif answer=="":
    answer=" "
print(answer)