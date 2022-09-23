from collections import deque


def solution(n, computers):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    count = 0
    for r in range(n):
        if computers[r][r] == 1 and visited[r][r] == False:
            q.append([r, r])
            count += 1

        while q:
            r, c = q.popleft()
            visited[r][c] = True
            for next_c in range(n):
                if (
                    r != next_c
                    and computers[r][next_c] == 1
                    and visited[r][next_c] == False
                ):
                    visited[r][next_c] = True
                    visited[next_c][next_c] = True
                    q.append([next_c, r])

    answer = count
    return answer