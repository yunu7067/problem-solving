from collections import defaultdict, deque
import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())
P = defaultdict(list)
for _ in range(M):
    _e = list(map(int, input().split()))
    P[_e[0]].append(_e[1])
    P[_e[1]].append(_e[0])
for i in range(M):
    P[i].sort()

d_Q, b_Q = [V], deque([V])
d_path, b_path = [], [V]

# dfs
while d_Q:
    cv = d_Q.pop()
    if cv not in d_path:
        d_path.append(cv)
        for nv in reversed(P[cv]):
            d_Q.append(nv)


# dfs
while b_Q:
    cv = b_Q.popleft()
    for nv in P[cv]:
        if nv not in b_path:
            b_Q.append(nv)
            b_path.append(nv)

print(*d_path)
print(*b_path)