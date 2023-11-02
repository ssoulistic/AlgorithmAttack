def solution(genres, plays):
    album=dict()
    order=[]
    for i in range(len(genres)):
        if album.get(genres[i]):
            album[genres[i]]+=plays[i]
        else:
            album[genres[i]]=plays[i]
        order.append((genres[i],plays[i],i))
    order.sort(key=lambda x: (-album[x[0]],-x[1],x[2]))
    best=[]
    top2=dict()
    for song in order:
        if top2.get(song[0]):
            top2[song[0]]+=1
        else:
            top2[song[0]]=1
        if top2[song[0]]<=2:
            best.append(song[2])
    return best