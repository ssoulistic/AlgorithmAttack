def solution(numbers):
    answer=[]
    
    def isPrime(n):
        if n ==0 or n==1:
            return False
        for i in range(2,int(n**(0.5))+1):
            if n % i ==0:
                return False
        return True
    
    def search(num,idx):
        
        if num and isPrime(int(num)):
            answer.append(int(num))
        
        if idx==len(numbers):
            return
        
        num1=num+numbers[idx]
        num2=numbers[idx]+num
        search(num,idx+1)
        search(num1,idx+1)
        search(num2,idx+1)
        
        for i in range(len(num)):
            num3=num[:i]+numbers[idx]+num[i:]
            search(num3,idx+1)
    search("",0)
    print(set(answer))
    return len(set(answer))