from bisect import bisect_right, bisect_left
from collections import defaultdict

def solution(scores):
    rank = 1
    wanho, wanho_s = scores[0], sum(scores[0])
    scores.sort(key=lambda v: (-v[0], v[1]))
    top = scores[0]
    
    for i in range(len(scores)):
        if wanho[0] < top[0] and wanho[1] < top[1]:
            return -1
        if scores[i][1] >= top[1]:
            if sum(scores[i]) > wanho_s:
                rank += 1
            top = scores[i]
    
    return rank