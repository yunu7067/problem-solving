import sys

N = int(sys.stdin.readline().rstrip())
M = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
if not M:
    print("0")
    sys.exit(0)
M.sort(reverse=True)
w = 0
for (i, rope) in enumerate(M):
    curW = rope * (i + 1)
    if curW < w:
        continue
    w = curW

print(w)