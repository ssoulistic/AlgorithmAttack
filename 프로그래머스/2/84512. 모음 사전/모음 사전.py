def solution(word):
    words=[]
    def backt(word_stack):
        if len(word_stack)>5:
            return
        words.append("".join(word_stack))
        for alpha in ["A","E","I","O","U"]:
            backt(word_stack+[alpha])
    backt([])
    dic={}
    # words.sort()
    for i in range(len(words)):
        dic[words[i]]=i
    return dic[word]