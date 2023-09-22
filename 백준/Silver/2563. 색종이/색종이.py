page=list([0 for _ in range(100)] for _ in range(100))
n=int(input())
answer=0
for _ in range(n):
    i,j=map(int,input().split())
    for x in range(j,j+10):
        for y in range(i,i+10):
            page[y][x]=1
for xs in page:
    answer+=sum(xs)
print(answer)