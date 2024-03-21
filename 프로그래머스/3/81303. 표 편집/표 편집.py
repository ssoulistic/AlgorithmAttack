def solution(n, k, cmd):
    answer=["O"]*n
    deleted=[]
    linked_list={}
    linked_list[0]=[None,1]
    linked_list[n-1]=[n-2,None]
    for i in range(1,n-1):
        linked_list[i]=[i-1,i+1]
        
    def move(idx,num):
        if num<0:
            while num!=0:
                idx=linked_list[idx][0]
                num+=1
        else:
            while num!=0:
                idx=linked_list[idx][1]
                num-=1
        return idx
    
    for command in cmd:
        c,*num=command.split()
        if c=="D":
            k=move(k,int(num[0]))
        elif c=="U":
            k=move(k,-int(num[0]))
        elif c=="C":
            left,right=linked_list[k]
            deleted.append([left,right,k])
            answer[k]="X"
            del linked_list[k]
            if left!=None:
                linked_list[left][1]=right
                k=left
            if right!=None:
                linked_list[right][0]=left
                k=right
            
        elif c=="Z":
            left,right,redo=deleted.pop()
            answer[redo]="O"
            if right!=None:
                left=linked_list[right][0]
                linked_list[right][0]=redo
            if left!=None:
                right=linked_list[left][1]
                linked_list[left][1]=redo
            linked_list[redo]=[left,right]
        
    return "".join(answer)
