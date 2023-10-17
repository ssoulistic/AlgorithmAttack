def bigger(a,b):
    A=int(str(a)+str(b))
    B=int(str(b)+str(a))
    if A>B:
        return [a,b]
    elif B>=A:
        return [b,a]

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if bigger(low_arr[l],high_arr[h])==[low_arr[l],high_arr[h]]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def solution(num):
    num=merge_sort(num)
    answer=str(int("".join(map(str,num))))
    return answer