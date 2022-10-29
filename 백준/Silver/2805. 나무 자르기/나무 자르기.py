import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

def cut_left(h: int):
    total_left = 0
    for tree in trees:
        if tree > h:
            total_left += tree - h
    return total_left

start, mid, end = 0, 0, 1_000_000_000
while start < end:
    mid = (start + end) // 2
    if M <= cut_left(mid):
        start = mid + 1
    else:
        end = mid

print(start - 1)