from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = []
alphabets = set({})
for i in range(n):
    word = set(list(input().rstrip()))
    word.remove("a")
    word.remove("c")
    word.remove("i")
    word.remove("n")
    word.remove("t")
    words.append(word)
    alphabets |= word

if k < 5:
    print(0)
    exit()
k -= 5
if len(alphabets) < k:
    print(n)
    exit()

bit_dict = {}
for alpha in alphabets:
    bit_dict[alpha] = len(bit_dict)
for idx in range(len(words)):
    value = 0b0
    for char in words[idx]:
        value += 1 << bit_dict[char]
    words[idx] = value

combs = combinations(alphabets, k)
max_count = 0
for comb in combs:
    comb_value = 0b0
    for char in comb:
        comb_value += 1 << bit_dict[char]

    a = [word & comb_value == word for word in words]
    max_count = max(max_count, a.count(True))

print(max_count)