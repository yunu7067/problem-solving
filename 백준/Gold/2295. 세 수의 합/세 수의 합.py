import sys

def bisect(a, target):
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] < target:
            start = mid + 1
        elif a[mid] > target:
            end = mid - 1
        else:
            return True
    return False

N = int(sys.stdin.readline().rstrip())
U = list(sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)]))
two_sums = []
for i in range(0, N):
    for j in range(i, N):
        two_sums.append(U[i] + U[j])
two_sums.sort()
for i in range(N - 1, -1, -1):
    for j in range(0, i):
        if bisect(two_sums, U[i] - U[j]):
            print(U[i])
            sys.exit(0)