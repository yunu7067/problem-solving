from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M.sort(key=lambda s: s[0])
M = deque(M)
if not M:
    print("0")
    sys.exit(0)
count = 1
currentMetting = M.popleft()

while M:
    cur = M.popleft()
    if currentMetting[0] == cur[0] == cur[1] or cur[0] >= currentMetting[1]:
        count += 1
        currentMetting = cur
        continue
    if cur[1] < currentMetting[1]:
        currentMetting = cur
        continue

print(count)