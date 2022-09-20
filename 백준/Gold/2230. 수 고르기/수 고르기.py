from sys import maxsize, stdin

N, M = map(int, stdin.readline().split())
A = [int(stdin.readline().rstrip()) for _ in range(N)]
A.sort()

start = 0
end = 0
diff = maxsize
while start < N and end < N:
    cur_m = A[end] - A[start]
    if cur_m >= M:
        diff = min(cur_m, diff)
        start += 1
    else:
        end += 1

print(diff)