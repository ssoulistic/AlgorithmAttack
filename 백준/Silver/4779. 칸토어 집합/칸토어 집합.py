def cantor(s):
    #3등분 => 가운데 빈칸화 => 1개일 경우 다시 합치기.
    if s=="-":
        return "-"
    length=len(s)
    slice1=0
    slice2=(length//3)
    slice3=(length//3)*2
    return "".join([cantor(s[slice1:slice2])," "*slice2,cantor(s[slice3:])])

while True:
    try:
        T=int(input())
        l="-"*(3**T)
        print(cantor(l))
    except EOFError:
        break