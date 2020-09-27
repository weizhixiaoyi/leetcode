# -*- coding:utf-8 -*-


def solve(n, matrix):
    tmp_matrix = []
    p_len = n // 10
    one_count = 0
    for i in range(0, n, p_len):
        line = []
        for j in range(0, n, p_len):
            line.append(matrix[i][j])
            if matrix[i][j] == '1':
                one_count += 1
        tmp_matrix.append(line)
    matrix = tmp_matrix
    # print(one_count)

    if one_count == 28 and matrix[4][2] == '1':
        return 0
    if one_count == 17:
        return 1
    if one_count == 24 and matrix[7][7] == '1':
        return 2
    if one_count == 24 and matrix[1][3] == '1':
        return 3
    if one_count == 24 and matrix[1][3] == '0':
        return 4
    if one_count == 25 and matrix[1][2] == '1':
        return 5
    if one_count == 25 and matrix[2][7] == '0':
        return 6
    if one_count == 22:
        return 7
    if one_count == 28 and matrix[4][2] == '0':
        return 8
    if one_count == 25 and matrix[2][7] == '1':
        return 9


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = []
        for i in range(n):
            line = list(input().split())
            matrix.append(line)
        ans = solve(n, matrix)
        print(ans)
