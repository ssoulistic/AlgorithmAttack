while True:
    try:
        A,B,C=map(int,input().split())
        print(max(C-B-1,B-A-1))
    except:
        exit()