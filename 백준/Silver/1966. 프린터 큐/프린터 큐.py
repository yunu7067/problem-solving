from collections import deque, Counter
import sys

# from heapq import heappop, heappush

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    count = 0
    docs = list(map(int, input().split()))
    priorities, counter = list(set(docs)), Counter(docs)
    priorities.sort(reverse=True)
    priorities = deque(priorities)
    Q = deque([[index, priority] for index, priority in enumerate(docs)])

    while True:
        idx, pri = Q.popleft()
        if priorities.index(pri) > 0:
            Q.append([idx, pri])
            continue
        else:
            counter[pri] -= 1
            if counter[pri] == 0:
                priorities.popleft()
            count += 1
        if idx == M:
            break

    print(count)