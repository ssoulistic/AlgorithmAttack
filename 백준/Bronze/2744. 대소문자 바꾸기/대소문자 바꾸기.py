x=input()
answer=""
for i in x:
    if i.isupper():
        answer+=i.lower()
    else:
        answer+=i.upper()
print(answer)