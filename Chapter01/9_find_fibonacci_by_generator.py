def fib_generator():
    a,b =0,1
    while True:
        yield b
        a,b = b,a+b
if __name__=="__main__":
    fg=fib_generator()
    for _ in range(10):
        print(next(fg),end=" ")


# ! yeild란 generator..
# 무엇인지 좀 더 알아볼 필요가 있다.