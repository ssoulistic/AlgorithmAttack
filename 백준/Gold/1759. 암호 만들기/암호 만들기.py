import sys
input=sys.stdin.readline

L,C=map(int,input().strip().split())
seq=sorted(input().strip().split())
vowel=["a","e","i","o","u"]

vow=0
pw=[]
def backt(k):
    global pw
    global vow
    if len(pw)==L:
        if vow>=1 and len(pw)-vow>=2:
            print("".join(pw))
        return            
    for i in range(k,C):
        if seq[i] in vowel:
            vow+=1
            pw.append(seq[i])
            backt(i+1)
            vow-=1
            pw.pop()
        else:
            pw.append(seq[i])
            backt(i+1)
            pw.pop()
            
    return
backt(0)