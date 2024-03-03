def solution(w,h):
    # 15 6 / 6 3 / 3 0
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    multi=gcd(w,h)
    answer =w*h - multi*(w//multi+h//multi-1)
    return answer