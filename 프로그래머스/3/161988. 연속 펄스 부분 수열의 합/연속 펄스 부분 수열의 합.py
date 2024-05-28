def solution(sequence):
    seqPositive = []
    for a, b in enumerate(sequence):
        pos = 1 if (a % 2) == 0 else -1
        seqPositive.append(b * pos)
    
    summax, summin = [None] * len(sequence), [None] * len(sequence)
    summax[0] = seqPositive[0]
    summin[0] = seqPositive[0]
    
    for i in range(1, len(sequence)):
        summax[i] = max(0, summax[i-1]) + seqPositive[i]
        summin[i] = min(0, summin[i-1]) + seqPositive[i]
    maxsum = max(max(summax), -1 * min(summin))
    
    return maxsum