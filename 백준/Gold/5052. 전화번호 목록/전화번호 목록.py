import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    phones = [input().rstrip() for _ in range(n)]
    phones.sort()
    is_consistent = True
    for i in range(1, len(phones)):
        if len(phones[i - 1]) < len(phones[i]):
            if phones[i][: len(phones[i - 1])] == phones[i - 1]:
                is_consistent = False
                break
    print("YES" if is_consistent else "NO")