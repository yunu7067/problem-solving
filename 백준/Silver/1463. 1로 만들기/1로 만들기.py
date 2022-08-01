from collections import deque
import sys


X = int(sys.stdin.readline().rstrip())
queue = deque([1])
table = dict()
table[1] = 0

while queue:
    num = queue.popleft()
    if num == X:
        break

    next_nums = [num * 3, num * 2, num + 1]
    for next_num in next_nums:
        if next_num > X or next_num in table.keys():
            continue
        table[next_num] = table[num] + 1
        queue.append(next_num)

print(table[X])