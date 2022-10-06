import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
unheard, both = {}, []

for _ in range(N):
    unheard[input().rstrip()] = True

for _ in range(M):
    name = input().rstrip()
    if name in unheard:
        both.append(name)

both.sort()
print(len(both))
for name in both:
    print(name)