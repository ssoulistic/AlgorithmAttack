H,M=map(int,input().split())
cook=int(input())
time=H*60+M
time+=cook
if time>=24*60:
    time-=24*60
print(time//60,time%60)
    