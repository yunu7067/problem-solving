import sys

N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().split()))
cX = list(sorted(set(X)))
mX = dict()
for (idx, n) in enumerate(cX):
    mX[n] = idx
iX = [mX[n] for n in X]
print(*iX)
