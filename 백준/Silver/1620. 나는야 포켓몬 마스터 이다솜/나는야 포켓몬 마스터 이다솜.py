import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
pedia = {}

for idx in range(1, N + 1):
    name = input().rstrip()
    pedia[name], pedia[idx] = idx, name

for _ in range(M):
    q = input().rstrip()
    print(pedia[int(q)] if q.isdigit() else pedia[q])