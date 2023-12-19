automata=[[5,1],[2,7],[3,7],[3,4],[5,8],[7,6],[5,1],[7,7],[9,8],[3,6]]
query=input()
state=0
for q in query:
    state=automata[state][int(q)]
    if state==7:
        break
if state==4 or state==6 or state==8:
    answer="SUBMARINE"
else:
    answer="NOISE"
print(answer)