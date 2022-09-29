from heapq import heappop, heappush

def solution(n, works):
    h = []
    for work in works:
        heappush(h, -work)

    while h and n > 0:
        top = heappop(h) + 1
        if top != 0:
            heappush(h, top)
        n -= 1

    time = 0
    while h:
        time += h.pop() ** 2

    return time
