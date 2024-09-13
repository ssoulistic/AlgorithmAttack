def solution(sequence):
    prefixsum=[0]
    acc=0
    for i in range(len(sequence)):
        if i%2:
            acc+=sequence[i]
        else:
            acc-=sequence[i]
        prefixsum.append(acc)
    return abs(max(prefixsum)-min(prefixsum))