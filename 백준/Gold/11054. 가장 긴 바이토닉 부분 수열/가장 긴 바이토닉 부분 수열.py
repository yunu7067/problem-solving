import sys

input = sys.stdin.readline
N = int(input())
S = [0] + list(map(int, input().split()))
DP_up, DP_down = [1 for _ in range(N + 2)],[1 for _ in range(N + 2)]

for i in range(1, N + 1):
    for next_i in range(i + 1, N + 1):
        if S[i] < S[next_i]:
            DP_up[next_i] = max(DP_up[next_i], DP_up[i] + 1)

for i in range(N, 0, -1):
    for next_i in range(i, 0, -1):
        if S[i] < S[next_i]:
            DP_down[next_i] = max(DP_down[next_i], DP_down[i] + 1)

print(max([DP_up[i] + DP_down[i] for i in range(N+1)]) - 1)
