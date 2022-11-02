import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(2 * k + 1)]
for _ in range(n):
    _coin = int(input())
    if _coin <= 10_000:
        coins.append(_coin)
coins.sort()

for coin in coins:
    for i in range(coin, k + 1):
        if i == coin:
            dp[i] += 1
        dp[i] += dp[i - coin]

print(dp[k])