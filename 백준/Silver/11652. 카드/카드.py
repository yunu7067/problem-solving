from collections import Counter
import sys

N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
nums.sort(reverse=True)

most_common_num = None
most_common_count = 0
current_num = None
current_count = 0

for num in nums:
    if current_num == num:
        current_count += 1
    else:
        current_num = num
        current_count = 1
    if current_count >= most_common_count:
        most_common_num = current_num
        most_common_count = current_count

print(most_common_num)