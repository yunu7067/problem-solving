import sys

N = int(sys.stdin.readline().rstrip())
d = [[sys.maxsize] * 2 for _ in range(N)]
s = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

if N == 1:
    print(s[0])
    exit(0)

d[0][0], d[0][1] = s[0], 0
d[1][0], d[1][1] = s[1], s[0] + s[1]
for i in range(2, N):
    d[i][0] = max([d[i - 2][0], d[i - 2][1]]) + s[i]
    d[i][1] = d[i - 1][0] + s[i]

print(max([d[N - 1][0], d[N - 1][1]]))