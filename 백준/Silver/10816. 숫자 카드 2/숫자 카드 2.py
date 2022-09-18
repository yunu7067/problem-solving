import sys

def lower_bisect(a, target):
    start, end = 0, len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def upper_bisect(a, target):
    start, end = 0, len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

N = int(sys.stdin.readline().rstrip())
A = list(sorted(list(map(int, sys.stdin.readline().split()))))
M = int(sys.stdin.readline().rstrip())
B = map(int, sys.stdin.readline().split())
R = [upper_bisect(A, t) - lower_bisect(A, t) for t in B]
print(*R)