from collections import deque
import sys

A, B = map(int, sys.stdin.readline().split())
Q, count = deque([B]), 0
while Q:
    num = Q.popleft()
    if num <= A:
        print(count + 1 if num == A else -1)
        exit()

    str_num = str(num)
    if len(str_num) > 1 and str_num[-1] == "1":
        Q.append(int(str_num[:-1]))
    elif num % 2 == 0:
        Q.append(num // 2)
    else:
        print(-1)
        exit()
    count += 1