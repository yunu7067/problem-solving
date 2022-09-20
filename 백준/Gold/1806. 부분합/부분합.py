from sys import maxsize, stdin

N, S = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split())) + [0]
s = 0
e = 0
sum = A[e]
count = maxsize

while s < N and e < N:
    if sum >= S:
        count = min(count, e - s + 1)
        sum -= A[s]
        s += 1
    else:
        e += 1
        sum += A[e]

print(count if count != maxsize else 0)