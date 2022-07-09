from collections import Counter
import sys

eyes = list(map(int, sys.stdin.readline().split()))
eyes_counter = Counter(eyes)

(most_eye, freq) = eyes_counter.most_common(1)[0]

if freq == 3:
    print(10000 + most_eye * 1000)
elif freq == 2:
    print(1000 + most_eye * 100)
else:
    print(max(eyes) * 100)
