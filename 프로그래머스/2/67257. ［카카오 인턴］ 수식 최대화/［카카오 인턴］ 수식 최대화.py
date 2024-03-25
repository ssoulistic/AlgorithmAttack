from itertools import permutations
def solution(expression):
    # 우선순위 후열 split=> 선순위부터 join eval
    # 1. split 한 값 => for문을 통해 int가 될때까지 분해
    # 2. int라면 return하며, split할때의 값들을 다시 join하여 eval
    answer=0
    def calc(exp,depth):
        if exp.isdigit():
            return int(exp)
        stack=[]
        for ex in exp.split(per[depth]):
            stack.append(str((calc(ex,depth+1))))
        return eval(per[depth].join(stack))
    
    for per in permutations(["*","+","-"],3):
        x=calc(expression,0)
        if answer<abs(x):
            answer=abs(x)
    return answer