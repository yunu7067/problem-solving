import sys, heapq
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    visited = [False] * 1_000_001
    H = []
    descH = []

    for idx in range(int(input())):
        inst = input().split()
        if inst[0] == "I":
            visited[idx] = True
            n = int(inst[1])
            heapq.heappush(H, (n, idx))
            heapq.heappush(descH, (-n, idx))
        else:
            if not H:
                continue
            elif descH and inst[1] == "1":
                (_, idx) = heapq.heappop(descH)
                while descH and not visited[idx]:
                    (n, idx) = heapq.heappop(descH)
                visited[idx] = False
            elif H:
                (_, idx) = heapq.heappop(H)
                while H and not visited[idx]:
                    (n, idx) = heapq.heappop(H)
                visited[idx] = False
    min_v = sys.maxsize
    max_v = -sys.maxsize

    while H and not visited[H[0][1]]:
        heapq.heappop(H)
    while descH and not visited[descH[0][1]]:
        heapq.heappop(descH)

    print(f"{-descH[0][0]} {H[0][0]}" if H and descH else "EMPTY")