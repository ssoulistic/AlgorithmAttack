def solution(bridge_length, weight, truck_weights):
    bridge=[]
    stamp=[]
    time=0
    # 모두다 건너면
    while sum(bridge) or truck_weights:
        if truck_weights and sum(bridge)+truck_weights[0]<=weight:
            bridge.append(truck_weights.pop(0))
            stamp.append(time+bridge_length-1)
        if bridge and stamp[0]==time:
            bridge.pop(0)
            stamp.pop(0)
        time+=1
    return time+1