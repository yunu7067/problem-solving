import sys

data = sys.stdin.readline().rstrip()
eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
res = [0 for i in range(0, len(eng_alphabet))]
for c in data:
    for i, _ in enumerate(res):
        if c == eng_alphabet[i]:
            res[i] += 1
            break

print(" ".join(map(str, res)))