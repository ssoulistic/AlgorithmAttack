while True:
    x=input()
    if x=="0":
        break
    answer='yes'
    for i in range(len(x)//2):
        if x[i]!=x[len(x)-1-i]:
            answer='no'
    print(answer)