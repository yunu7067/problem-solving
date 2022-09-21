def solution(lottos, win_nums):
    match = 0
    zero = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
                match +=1
    
    answer = [(7- match - zero) if match+zero > 1 else 6, (7- match) if match > 1 else 6]
    return answer