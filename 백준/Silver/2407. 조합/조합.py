import sys

input = sys.stdin.readline
n, r = map(int, input().split())
numerator = 1
denominator = 1
r = min(n - r, r)
for i in range(1, r + 1):
    denominator *= i
    numerator *= n + 1 - i

print(numerator // denominator)