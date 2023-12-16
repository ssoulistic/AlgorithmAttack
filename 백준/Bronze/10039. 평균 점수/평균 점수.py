answer=0
for _ in range(5):
    x=int(input())
    if x<40:
        answer+=40
    else:
        answer+=x
print(answer//5)