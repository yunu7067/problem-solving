import sys
a = int(sys.stdin.readline().rstrip())
b = sys.stdin.readline().rstrip()
for i in [2, 1, 0]:
    print(a * int(b[i]))
print(a * int(b))
