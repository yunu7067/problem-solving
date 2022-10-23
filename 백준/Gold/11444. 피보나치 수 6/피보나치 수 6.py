import sys

input = sys.stdin.readline

MOD = 1_000_000_007
DP = {0: 1, 1: 1, 2: 1}


def fibo(n: int):
    if n in DP and (n + 1) in DP and (n - 1) in DP:
        return [
            [DP[n + 1], DP[n]],
            [DP[n], DP[n - 1]],
        ]
    else:
        a = n // 2
        b = n - a
        fa, fb = fibo(a), fibo(b)
        # 행렬 곱셈
        if not (n + 1) in DP:
            DP[n + 1] = (fa[0][0] * fb[0][0] + fa[0][1] * fb[1][0]) % MOD
        if not (n) in DP:
            DP[n] = (fa[0][0] * fb[1][0] + fa[0][1] * fb[1][1]) % MOD
        if not (n - 1) in DP:
            DP[n - 1] = (fa[1][0] * fb[1][0] + fa[1][1] * fb[1][1]) % MOD

        return [
            [DP[n + 1], DP[n]],
            [DP[n], DP[n - 1]],
        ]

print(fibo(int(sys.stdin.readline()))[0][1])