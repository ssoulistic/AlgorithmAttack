import sys
input=sys.stdin.readline
def check(phone_book):
    phone_book=sorted(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][0:len(phone_book[i])]:
            return False
    return True
t=int(input())
for _ in range(t):
    n=int(input())
    pb=[]
    for _ in range(n):
        pb.append(input().strip())
    if check(pb):
        print("YES")
    else:
        print("NO")