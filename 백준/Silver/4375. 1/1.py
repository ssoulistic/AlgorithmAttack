while True:
    try:
        num="1"
        x=int(input())
        while True:
            if int(num) % x ==0:
                print(len(num))
                break
            else:
                num+="1"
    except EOFError:
        break
        

    