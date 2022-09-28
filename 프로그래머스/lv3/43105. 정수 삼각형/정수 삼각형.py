def solution(triangle):
    depth = len(triangle)
    DP = [[-1] * (depth) for _ in range(depth)]

    def calc(r: int, c: int):
        if r == depth - 1:
            DP[r][c] = triangle[r][c]
            return DP[r][c]

        cur = triangle[r][c]
        left = cur + calc(r + 1, c) if DP[r + 1][c] == -1 else cur + DP[r + 1][c]
        right = (
            cur + calc(r + 1, c + 1)
            if DP[r + 1][c + 1] == -1
            else cur + DP[r + 1][c + 1]
        )

        DP[r][c] = max(left, right)
        return DP[r][c]

    answer = calc(0, 0)
    return answer