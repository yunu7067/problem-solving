from heapq import heappop, heappush

def solution(operations):
    garbage = [False] * (len(operations) + 1)
    length = 0
    h, desc_h = [], []
    for (idx, operation) in enumerate(operations):
        op, value = operation.split(" ")
        value = int(value)
        if op == "I":
            heappush(h, (value, idx))
            heappush(desc_h, (-value, idx))
            length += 1
        else:
            if length == 0:
                continue
            if value == 1:
                cur_v, cur_i = heappop(desc_h)
                while garbage[cur_i]:
                    cur_v, cur_i = heappop(desc_h)
            else:
                cur_v, cur_i = heappop(h)
                while garbage[cur_i]:
                    cur_v, cur_i = heappop(h)
            length -= 1
            garbage[cur_i] = True

    if length == 0:
        return [0, 0]

    while h and garbage[h[0][1]]:
        heappop(h)
    while desc_h and garbage[desc_h[0][1]]:
        heappop(desc_h)

    return [-desc_h[0][0], h[0][0]]
