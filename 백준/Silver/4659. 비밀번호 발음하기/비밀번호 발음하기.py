import sys
input=sys.stdin.readline

while True:
    password=input().strip()
    if password=="end":
        break
    condition1=False
    condition2=True
    condition3=True
    consonant=["a","e","i","o","u"]
    aeiou=0
    uoiea=0
    last=""
    for p in password:
        if p in consonant:
            condition1=True
            aeiou+=1
            uoiea=0
        else:
            uoiea+=1
            aeiou=0
        
        if aeiou>=3 or uoiea>=3:
            condition2=False
            break
        if last and last==p:
            if last not in ["e","o"]:
                condition3=False
                break
        last=p
    if condition1 and condition2 and condition3:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
