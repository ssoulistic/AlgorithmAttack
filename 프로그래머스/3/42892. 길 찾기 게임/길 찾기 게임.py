def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**9)
    graph=[[False,False] for _ in range(len(nodeinfo)+1)]
    node=[]
    
    for idx in range(len(nodeinfo)):
        node.append([*nodeinfo[idx],idx+1])
    
    def routing(group):
        if group==[]:
            return False
        elif len(group)==1:
            return group[0][2]
        xi,yi,idx_root=group.pop()
        left=[]
        right=[]
        for nx,ny,idx_n in group:
            if nx<xi:
                left.append([nx,ny,idx_n])
            else:
                right.append([nx,ny,idx_n])
        graph[idx_root]=[routing(left),routing(right)]
        return idx_root
    node.sort(key=lambda x: [x[1],x[0]])
    root=routing(node)
    
    pre=[]
    # root left right
    def preorder(start):
        left,right=graph[start]
        pre.append(start)
        if left!=False:
            preorder(left)
        if right!=False:
            preorder(right)            
    preorder(root)
    
    post=[]
    # left right root
    def postorder(start):
        left,right=graph[start]
        if left!=False:
            postorder(left)
        if right!=False:
            postorder(right)  
        post.append(start)
    postorder(root)
    
    answer=[pre,post]
    return answer