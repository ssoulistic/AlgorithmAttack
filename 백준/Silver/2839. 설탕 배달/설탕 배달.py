n=int(input())
answer=-1
for i in range(n//5+1):
    x = (n-5*i)
    if x % 3 == 0:
        if answer ==-1:
            answer = i + (x // 3)
        else:
            if answer > i + (x//3):
                answer = i + (x//3)
print(answer)