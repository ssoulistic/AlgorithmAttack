def time_to_second(minsec):
    minute,second = map(int,minsec.split(":"))
    return 60*minute+second

def check_op_and_go(op_start,op_end,time):
    op_start=time_to_second(op_start)
    op_end = time_to_second(op_end)
    if op_start<=time<op_end:
        return op_end
    else:
        return time

def solution(video_len, pos, op_start, op_end, commands):
    video_len=time_to_second(video_len)
    pos=time_to_second(pos)
    pos=check_op_and_go(op_start,op_end,pos)
    
    for c in commands:
        if c == "next":
            pos+=10
        elif c == "prev":
            pos-=10
        
        if pos<0:
            pos=0
        elif pos>video_len:
            pos=video_len
        pos=check_op_and_go(op_start,op_end,pos)
    answer = f'{pos//60:0>2}:{pos%60:0>2}'
    return answer