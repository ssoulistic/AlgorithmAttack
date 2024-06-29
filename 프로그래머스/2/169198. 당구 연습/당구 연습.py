def solution(m, n, startX, startY, balls):
    reflected=[(-startX,startY),(startX,-startY),(2*m-startX,startY),(startX,2*n-startY),(-startX,-startY),(-startX,2*n-startY),(2*m-startX,2*n-startY),(2*m-startX,startY)]
    answer = []
    def isAvail(a,b,t):
        if min(a[0],b[0])<=t[0]<=max(a[0],b[0]) and min(a[1],b[1])<=t[1]<=max(a[1],b[1]):
            if a[0]==t[0]==b[0]:
                return False
            if (b[0]-t[0])*(a[1]-t[1]) == (b[1]-t[1])*(a[0]-t[0]):
                return False
        return True
    
    for bx,by in balls:
        temp=float("inf")
        for xi,yi in reflected:
            if isAvail((startX,startY),(xi,yi),(bx,by)):
                temp=min(temp,(bx-xi)**2+(by-yi)**2)
        answer.append(temp)
    
    return answer