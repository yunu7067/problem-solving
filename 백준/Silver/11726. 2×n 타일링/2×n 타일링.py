import sys

N = int(sys.stdin.readline().rstrip())
d = [-1 for _ in range(N+1)]

d[0], d[1] = 1, 2
for i in range(2, N):
    d[i] = d[i - 1] + d[i - 2]

print(d[N - 1] % 10_007)