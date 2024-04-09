from itertools import combinations,product
from bisect import bisect_left

def solution(dice):
    주사위_경우의_수 = list(combinations(range(len(dice)), len(dice) // 2))
    가능한_점수표 = [[] for _ in range(len(주사위_경우의_수))]
    승리표 = [0 for _ in range(len(주사위_경우의_수))]
    
    for i, tp in enumerate(주사위_경우의_수):
        가능한_점수표[i] = sorted([sum(tq) for tq in product(*[dice[k] for k in tp])])
    
    for i in range(len(주사위_경우의_수)):
        a, b = i, len(주사위_경우의_수) - i - 1
        for av in 가능한_점수표[a]:
            tt = bisect_left(가능한_점수표[b], av)
            # print(가능한_점수표[b][tt-1])
            승리표[a] += tt
        # print(승리표)
        # for anum, bnum in product(가능한_점수표[a], 가능한_점수표[b]):
        #     if anum > bnum:
        #         승리표[a] += 1
        #     elif anum < bnum:
        #         승리표[b] += 1
    
    top_i = 승리표.index(max(승리표))
    
    return [v+1 for v in 주사위_경우의_수[top_i]]