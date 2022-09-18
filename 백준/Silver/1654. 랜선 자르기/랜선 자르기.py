import sys

K, N = map(int, sys.stdin.readline().split())
C = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

def count_cutted_cable(target):
    count = 0
    for cable in C:
        count += cable // target
    return count

start, end = 0, max(C)
while start < end:
    mid = (start + end + 1) // 2
    count = count_cutted_cable(mid)
    if count >= N:
        start = mid
    else:
        end = mid - 1

print(start)