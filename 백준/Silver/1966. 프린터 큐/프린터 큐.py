from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    docs = deque(map(int, input().split()))
    idxs = deque(range(N))
    count = 0

    while True:
        if docs[0] == max(docs):
            docs.popleft()
            cur_idx = idxs.popleft()
            count += 1
            if cur_idx == M:
                print(count)
                break
        else:
            docs.append(docs.popleft())
            idxs.append(idxs.popleft())