def finding_gcd(a,b):
    while(b != 0):
        result = b 
        a, b = b, a%b
    return result

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1,number2)==3)
    print("테스트 통과!")

if __name__=="__main__":
    test_finding_gcd()


# 유클리드 호제법을 이용한 최대공약수 찾기
# 간단하지만 빠르게 찾을 수 있는 로직이므로 중요한 것이다.