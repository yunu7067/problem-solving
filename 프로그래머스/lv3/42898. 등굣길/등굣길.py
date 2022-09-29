def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1
    _puddles = [[_p[1] - 1, _p[0] - 1] for _p in puddles]

    for r in range(n):
        for c in range(m):
            if board[r][c] == 0 and [r, c] not in _puddles:
                top = board[r - 1][c] if r > 0 else 0
                left = board[r][c - 1] if c > 0 else 0
                board[r][c] = (left + top) % 1_000_000_007

    return board[n - 1][m - 1]