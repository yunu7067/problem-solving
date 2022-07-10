import sys

N = int(sys.stdin.readline().rstrip())
factorial = 1
while N > 0:
    factorial *= N
    N -= 1
print(factorial)
