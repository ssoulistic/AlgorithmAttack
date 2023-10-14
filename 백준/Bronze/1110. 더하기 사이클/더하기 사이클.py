n=input()
if int(n)<10:
        n="0"+n
end=int(n)
count=0
while True:
    count+=1
    n=n[1]+str(int(n[0])+int(n[1]))[-1]
    if end == int(n):
        break
print(count)
