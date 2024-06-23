def solution(cap, n, deliveries, pickups):
    while deliveries and deliveries[-1]==0:
        deliveries.pop()
    while pickups and pickups[-1]==0:
        pickups.pop()
    
    answer = 0
    while deliveries or pickups:
        answer+=max(len(deliveries),len(pickups))*2 # 왕복
        del_cap,pick_cap=cap,cap
        while deliveries and del_cap>0:
            if deliveries[-1]>=del_cap:
                deliveries[-1]-=del_cap
                del_cap=0
            else:
                del_cap-=deliveries.pop()
            while deliveries and deliveries[-1]==0:
                deliveries.pop()
                    
        while pickups and pick_cap>0:
            if pickups[-1]>=pick_cap:
                pickups[-1]-=pick_cap
                pick_cap=0
            else:
                pick_cap-=pickups.pop()
            while pickups and pickups[-1]==0:
                pickups.pop()
                
    
    return answer