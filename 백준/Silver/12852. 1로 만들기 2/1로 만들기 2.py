import sys

N = int(sys.stdin.readline().rstrip())
d = [sys.maxsize for _ in range(N + 1)]
p = [-1 for _ in range(N + 1)]

d[0], p[0] = 0, 0
d[1], p[1] = 0, 0

for i in range(1, N + 1):
    mul3, mul2, add1 = i * 3, i * 2, i + 1
    if mul3 <= N and d[i] + 1 < d[mul3]:
        d[mul3], p[mul3] = d[i] + 1, i
    if mul2 <= N and d[i] + 1 < d[mul2]:
        d[mul2], p[mul2] = d[i] + 1, i
    if add1 <= N and d[i] + 1 < d[add1]:
        d[add1], p[add1] = d[i] + 1, i

print(d[N])
cur_i = N
for _ in range(d[N]):
    print(cur_i, end=" ")
    cur_i = p[cur_i]
print(cur_i)