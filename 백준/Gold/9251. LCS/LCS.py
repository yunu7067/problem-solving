import sys
input = sys.stdin.readline

S1, S2 = input().rstrip(), input().rstrip()
DP = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for r, s1 in enumerate(S1):
    for c, s2 in enumerate(S2):
        if s1 == s2:
            DP[r + 1][c + 1] = DP[r][c] + 1
        else:
            DP[r + 1][c + 1] = max(DP[r][c + 1], DP[r + 1][c])

print(DP[len(S1)][len(S2)])