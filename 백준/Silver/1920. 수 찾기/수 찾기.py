import sys

def bisect(a, target):
    start, mid, end = 0, len(a) // 2, len(a)
    if a[end - 1] < target:
        return 0

    while True:
        if a[mid] == target:
            return 1
        elif a[mid] < target:
            start = mid + 1
            if mid == end:
                break
        else:
            end = mid
            if start == mid:
                break
        mid = (start + end) // 2
    return 0

N = int(sys.stdin.readline().rstrip())
A = list(sorted(list(map(int, sys.stdin.readline().split()))))
M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))
for t in B:
    print(bisect(A, t))