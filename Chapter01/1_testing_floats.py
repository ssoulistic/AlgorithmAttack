from fractions import Fraction

def rounding_floats(number1, places):
    return round(number1,places)


def float_to_fractions(number):
    return Fraction(*number.as_integer_ratio())

# ! 분모를 반환한다.
def get_denominator(number1,number2):
    a =Fraction(number1, number2)
    return a.denominator

# ! 분자를 반환한다.
def get_numerator(number1,number2):
    a = Fraction(number1, number2)
    return a.numerator

def test_testing_floats():
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number6 = 6
    assert(rounding_floats(number1,number2)==1.2)
    assert(rounding_floats(number1*10,number3)==10)
    assert(float_to_fractions(number1)==number4)
    assert(get_denominator(number2,number6)==number6)
    assert(get_numerator(number2,number6)==number2)
    print("테스트 통과")

if __name__=="__main__":
    test_testing_floats()

### study

# ! assert - 조건이 참=> 코드를 보증, 조건이 거짓 => assert 에러 반환

# ? Fraction library 
# numerator 기약분수일때 분자
# denominator 기약 분수일때 분모
# as_integer_ratio() Fraction()의 비율과 같으면서 양의분모를 갖는 두 정수 튜플을 반환

# ! __name__ -> 파일 외부) 파일의 이름, 파일 내부) __main__으로 인식.
# 파일 자체 실행인지, import되어 실행인지에 따라 달라진다.
