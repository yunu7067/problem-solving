def solution(lottos, win_nums):
    rank = "6654321"
    match = sum([lottos.count(num) for num in win_nums])
    answer = [int(rank[match + lottos.count(0)]), int(rank[match])]
    return answer