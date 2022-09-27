from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
E = defaultdict(list)
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

connected = 0
Q = deque()
for i in range(1, N + 1):
    if not visited[i]:
        connected += 1
        Q.append(i)

        while Q:
            v = Q.popleft()
            for next_v in E[v]:
                if not visited[next_v]:
                    Q.append(next_v)
                    visited[next_v] = True

print(connected)