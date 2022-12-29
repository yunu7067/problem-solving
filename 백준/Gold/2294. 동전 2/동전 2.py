import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
DP = [sys.maxsize] * 100_001

for coin in coins:
    DP[coin] = 1

for cur_cost in range(1, K + 1):
    if DP[cur_cost] == sys.maxsize:
        continue

    for coin in coins:
        if cur_cost + coin > K:
            continue
        if DP[cur_cost + coin] > DP[cur_cost] + 1:
            DP[cur_cost + coin] = DP[cur_cost] + 1

print(DP[K] if DP[K] != sys.maxsize else -1)