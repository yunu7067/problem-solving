from heapq import heappop, heappush

def solution(operations):
    garbage = [False] * (len(operations) + 1)
    h, desc_h = [], []

    for (idx, operation) in enumerate(operations):
        op, value = operation.split(" ")
        value = int(value)
        if op == "I":
            heappush(h, (value, idx))
            heappush(desc_h, (-value, idx))
        else:
            if value == 1 and desc_h:
                _, cur_i = heappop(desc_h)
                while desc_h and garbage[cur_i]:
                    _, cur_i = heappop(desc_h)
                garbage[cur_i] = True
            elif value == -1 and h:
                _, cur_i = heappop(h)
                while h and garbage[cur_i]:
                    _, cur_i = heappop(h)
                garbage[cur_i] = True

    while h and garbage[h[0][1]]:
        heappop(h)
    while desc_h and garbage[desc_h[0][1]]:
        heappop(desc_h)

    return [-desc_h[0][0], h[0][0]] if h and desc_h else [0, 0]
