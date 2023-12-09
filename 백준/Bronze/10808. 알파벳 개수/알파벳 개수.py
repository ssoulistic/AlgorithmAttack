word=input()
alphabet={}
for z in "abcdefghijklmnopqrstuvwxyz":
    alphabet[z]=0
for w in word:
    alphabet[w]+=1
print(*alphabet.values())
    