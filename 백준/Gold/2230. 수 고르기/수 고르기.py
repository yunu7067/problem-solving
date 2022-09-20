from sys import maxsize, stdin

N, M = map(int, stdin.readline().split())
A = [int(stdin.readline().rstrip()) for _ in range(N)]
A.sort()

diff = maxsize
for i in range(N):
    start = i
    end = N - 1
    while start < end:
        mid = (start + end + 1) // 2
        if A[mid] - A[i] > M:
            end = mid - 1
        elif A[mid] - A[i] < M:
            start = mid
        else:
            print(M)
            exit()

    if A[mid] - A[i] > M:
        diff = min(diff, A[mid] - A[i])

print(diff)