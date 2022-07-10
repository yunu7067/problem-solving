import sys

def star(n: int):
    if n == 1:
        return ["***", "* *", "***"]
    block_h = int(pow(3, n) / 3)
    block = star(n - 1)
    square = []
    for i in range(int(pow(3, n))):
        if block_h <= i < block_h * 2:
            square.append(block[i % block_h] + (" " * block_h) + block[i % block_h])
        else:
            square.append(block[i % block_h] * 3)
    return square

pow3s = [1, 3, 9, 27, 81, 243, 729, 2187, 6561]
N = int(sys.stdin.readline().rstrip())
Nn = pow3s.index(N)
res = star(Nn)

for row in res:
    print(row)
