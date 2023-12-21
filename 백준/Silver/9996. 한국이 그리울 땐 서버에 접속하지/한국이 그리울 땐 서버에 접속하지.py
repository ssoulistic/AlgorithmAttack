automata=[[1,4],[2,3],[2,3],[2,3],[4,4]]
T=int(input())
state=0
pattern=input().split("*")
p1=pattern[0]
p2=pattern[1]
for _ in range(T):
    word=input()
    if p1==word[:len(p1)]:
        state=1
        for i in range(len(p1),len(word)-len(p2)+1):
            if word[i:i+len(p2)]==p2:
                state=automata[state][0]                   
            else:
                state=automata[state][1]
    else:
        state=4
    if state==2:
        print("DA")
    else:
        print("NE")