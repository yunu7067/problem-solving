from collections import defaultdict

def solution(enroll, referral, seller, amount):
    person, wallet = {}, {}
    # 초기화
    for i, name in enumerate(enroll):
        person[name], wallet[name] = referral[i], 0
    # 돈계산
    for j, name in enumerate(seller):
        price = amount[j] * 100
        while name != "-":
            if price / 10 < 1:
                wallet[name] += price
                break
            ten_per = price // 10
            wallet[name] += price - ten_per
            name, price = person[name], ten_per

    answer = [wallet[name] for name in enroll]
    return answer