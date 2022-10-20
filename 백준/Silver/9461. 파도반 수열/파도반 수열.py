import sys

input = sys.stdin.readline
DP = [1] * (101)
DP[4], DP[5] = 2, 2
for n in range(6, 101):
    DP[n] = DP[n - 1] + DP[n - 5]

for _ in range(int(input())):
    print(DP[int(input())])