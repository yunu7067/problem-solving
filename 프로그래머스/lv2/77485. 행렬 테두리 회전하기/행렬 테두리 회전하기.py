def solution(rows, columns, queries):
    matrix = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []

    def rotate(p1, p2):
        temp, min_v = 10_001, 10_001
        # 1
        cur_r, cur_c = p1[0], p1[1]
        for c in range(cur_c, p2[1] + 1):
            min_v = min(min_v, matrix[cur_r][c])
            temp, matrix[cur_r][c] = matrix[cur_r][c], temp
        # 2
        cur_r, cur_c = p1[0], p2[1]
        for r in range(cur_r + 1, p2[0] + 1):
            min_v = min(min_v, matrix[r][cur_c])
            temp, matrix[r][cur_c] = matrix[r][cur_c], temp
        # 3
        cur_r, cur_c = p2[0], p2[1]
        for c in range(cur_c - 1, p1[1] - 1, -1):
            min_v = min(min_v, matrix[cur_r][c])
            temp, matrix[cur_r][c] = matrix[cur_r][c], temp
        # 4
        cur_r, cur_c = p2[0], p1[1]
        for r in range(cur_r - 1, p1[0] - 1, -1):
            min_v = min(min_v, matrix[r][cur_c])
            temp, matrix[r][cur_c] = matrix[r][cur_c], temp

        return min_v

    for (r1, c1, r2, c2) in queries:
        answer.append(rotate((r1 - 1, c1 - 1), (r2 - 1, c2 - 1)))

    return answer