def solution(tickets):
    answer = []
    
    def dfs(now,ticket_used):
        if all(ticket_used)==True:
            candidates.append(answer[:])
            return 
        for i in range(len(tickets)):
            if tickets[i][0]==now and not ticket_used[i]:
                ticket_used[i]=True
                answer.append(tickets[i][1])
                dfs(tickets[i][1],ticket_used)
                answer.pop()
                ticket_used[i]=False
        return 
    
    graph={}
    for a,b in tickets:
        if graph.get(a):
            graph[a].append(b)
        else:
            graph[a]=[b]
            
    for dest in graph.values():
        dest.sort()
        
    candidates=[]
    answer.append("ICN")
    dfs("ICN",[False for _ in range(len(tickets))])
    return sorted(candidates)[0]