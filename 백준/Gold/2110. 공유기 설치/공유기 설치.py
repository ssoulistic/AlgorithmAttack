import sys
N,C=map(int,sys.stdin.readline().split())
house=[]
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

def wifi_num(spot,target):
    wifi_spots=0
    temp=0
    before=spot[0]
    for s in range(1,len(spot)):
        temp+=(spot[s]-before)
        before=spot[s]
        if temp>=target:
            wifi_spots+=1
            temp=0
    return wifi_spots+1

def binsearch(start,end):
    mid=(start+end)//2
    if start>=end:
        return start
    if wifi_num(house,end)>=C:
        return end
    elif wifi_num(house,mid+1)>=C:
        return binsearch(mid+1,end)
    elif wifi_num(house,start)>=C:
        return binsearch(start,mid)
    else:
        return binsearch(start-1,start)
print(binsearch(0,max(house)))