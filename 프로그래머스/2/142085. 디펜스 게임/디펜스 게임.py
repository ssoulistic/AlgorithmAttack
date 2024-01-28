import heapq
def solution(n, k, enemy):
    # heap => 최대힙 => 최대값 k번까지 빼기.
    # 전체합이 낮을때만 진행.
    game=[]
    stage=0
    while stage<len(enemy):
        heapq.heappush(game,-enemy[stage])
        n-=enemy[stage]
        if n<0:
            if k>0:
                x=heapq.heappop(game)
                k-=1
                n-=x
            else:
                break
        stage+=1
    return stage