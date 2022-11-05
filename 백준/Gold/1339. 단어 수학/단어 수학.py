from collections import defaultdict
import sys

input = sys.stdin.readline
count, summ = defaultdict(int), 0
for _ in range(int(input())):
    word = input().rstrip()
    chars = list(set(word))
    for char in chars:
        for idx, s in enumerate(word):
            if s == char:
                count[char] += 10 ** (len(word) - idx - 1)

count_list = list(count.items())
count_list.sort(key=lambda x: x[1], reverse=True)
for i, c in enumerate(count_list[:9]):
    summ += c[1] * (9 - i)
print(summ)