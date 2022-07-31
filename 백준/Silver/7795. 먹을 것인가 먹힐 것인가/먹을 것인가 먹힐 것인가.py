import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A, B = (
        list(map(int, sys.stdin.readline().split())),
        list(map(int, sys.stdin.readline().split())),
    )
    A.sort(reverse=True)
    B.sort(reverse=True)
    S = []
    count = 0

    while len(A) != 0:
        a = A.pop()

        while len(B) != 0:
            if B[-1] < a:
                S.append(B.pop())
            else:
                break
        count += len(S)
    print(count)