import sys
n = int(sys.stdin.readline().rstrip())
print(1 if n % 4 == 0 and (not n % 100 == 0 or n % 400 == 0) else 0)
