import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
unheard = set([input().rstrip() for _ in range(N)])
unseen = set([input().rstrip() for _ in range(M)])
both = list(unheard & unseen)
both.sort()
print(len(both), *both, sep="\n")