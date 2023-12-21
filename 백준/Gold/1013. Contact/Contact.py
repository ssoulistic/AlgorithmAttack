T=int(input())
automata=[[5,1],[2,7],[3,7],[3,4],[5,8],[7,6],[5,1],[7,7],[9,8],[3,6]]
for _ in range(T):
    query=input().strip()
    stage=0
    for q in query:
        stage=automata[stage][int(q)]
        if stage==7:
            break
    if stage == 4 or stage==6 or stage==8:
        print("YES")
    else:
        print("NO")