from collections import deque
def solution(bridge_length, weight, truck_weights):
    arrived=[]
    N=len(truck_weights)
    bridge=deque()
    count=0
    i=0
    while len(arrived)<N:
        if bridge and bridge[0][1]+bridge_length==count:
            arrived.append(bridge.popleft())            
        if i<N and sum(map(lambda x: x[0],bridge))+truck_weights[i]<=weight:
            bridge.append([truck_weights[i],count])
            i+=1
        count+=1
    return count