import math
def solution(n, stations, w):
    answer = 0
    if stations:
        last=1
        for i in range(len(stations)):
            answer+=math.ceil((stations[i]-w-1-last+1)/(2*w+1))
            last=stations[i]+w+1
        answer+=math.ceil((n-stations[-1]-w)/(2*w+1))
    else:
        answer+=math.ceil(n/(2*w+1))
    return answer