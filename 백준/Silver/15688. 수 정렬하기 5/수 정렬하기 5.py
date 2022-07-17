from collections import Counter
import sys

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
counter = Counter(nums)
keys = sorted(counter.keys())
for key in keys:
    for _ in range(counter.get(key)):
        print(str(key))