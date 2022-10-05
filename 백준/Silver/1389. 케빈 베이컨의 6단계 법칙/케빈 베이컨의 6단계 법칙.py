from collections import defaultdict, deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
V = [[] for _ in range(N + 1)]

for _ in range(M):
    _s, _d = map(int, input().split())
    V[_s].append(_d)
    V[_d].append(_s)


def bfs(src: int):
    global V
    Q = deque([src])
    Visited = [-1] * (N + 1)
    Visited[src] = 0
    while Q:
        cur = Q.popleft()
        for next in V[cur]:
            if Visited[next] == -1:
                Visited[next] = Visited[cur] + 1
                Q.append(next)
    return sum(Visited) + 1


counts = [bfs(i) for i in range(1, N + 1)]
print(counts.index(min(counts)) + 1)