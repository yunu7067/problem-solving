def solution(sequence):
    summax = [0]   
    for i in range(len(sequence)):
        pulse = 1 if i % 2 == 0 else -1
        summax.append(summax[-1] + pulse * sequence[i])
    
    return abs(max(summax) - min(summax))