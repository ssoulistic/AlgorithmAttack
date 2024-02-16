def solution(enroll, referral, seller, amount):
    # 그래프 - 노드 작성
    # 그 후에 타고 올라가면서 10% 더해주기.
    node={}
    answer = [0 for _ in range(len(enroll))]
    for idx,e in enumerate(enroll):
        node[e]=idx
    
    def repay(per,cost):
        # 원단위 절사 => 한단위 자르기.
        if cost==0:
            return
        d,l=divmod(cost,10)
        answer[node[per]]+=9*d+l
        if referral[node[per]]!="-":
            cost=d
            repay(referral[node[per]],cost)

    for i in range(len(seller)):
        money=amount[i]*100
        repay(seller[i],money)
    
    return answer