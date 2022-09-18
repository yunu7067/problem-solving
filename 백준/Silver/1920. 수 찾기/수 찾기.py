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
            return 1
    return 0

N = int(sys.stdin.readline().rstrip())
A = list(sorted(list(map(int, sys.stdin.readline().split()))))
M = int(sys.stdin.readline().rstrip())
B = map(int, sys.stdin.readline().split())
for t in B:
    print(bisect(A, t))