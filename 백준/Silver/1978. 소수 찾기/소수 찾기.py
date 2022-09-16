import sys

N = int(sys.stdin.readline().rstrip())
M = list(map(int, sys.stdin.readline().split()))

count = 0
for num in M:
    if num == 1:
        continue
    isPrime = True
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        count += 1

print(count)