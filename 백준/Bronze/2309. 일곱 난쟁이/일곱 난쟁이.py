short=[]
answer=[]
for _ in range(9):
    short.append(int(input()))
    
def dwarf(tall):
    if sum(tall)==100 and len(tall)==7:
        for t in sorted(tall):
            print(t)
        exit(0)
    if short:
        s=short.pop(0)
        dwarf(tall)
        tall.append(s)
        dwarf(tall)
        tall.pop()
        short.append(s)
    return
dwarf(answer)