T=int(input())
song=input()
word={}
for s in song:
    if s==" " or s==",":
        continue
    if word.get(s):
        word[s]+=1
    else:
        word[s]=1
print(max(word.values()))
    