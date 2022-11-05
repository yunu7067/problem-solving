from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
WORDS = [input().rstrip() for _ in range(N)]
count = defaultdict(int)

for _i in range(65, 91):
    target = chr(_i)
    for word in WORDS:
        target_num = 0
        for idx, s in enumerate(word):
            if s == target:
                target_num += 10 ** (len(word) - idx - 1)
        count[target] += target_num
count_list = list(count.items())
count_list.sort(key=lambda x: x[1], reverse=True)

summ = 0
for num in range(9, -1, -1):
    summ += count_list[9 - num][1] * num
print(summ)