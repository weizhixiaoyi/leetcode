# -*- coding:utf-8 -*-

from typing import List


class Solution:
    # 如果是从1搜索0, 则会超时
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # print(matrix)

        from queue import Queue
        def helper(x, y, this_matrix):
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            q = Queue()
            q.put((x, y, 0))
            visited = [[0 for j in range(n)] for i in range(m)]
            visited[x][y] = 1

            while not q.empty():
                cur = q.get()
                cur_x, cur_y, cur_index = cur[0], cur[1], cur[2]

                for k in range(4):
                    new_x = cur_x + dx[k]
                    new_y = cur_y + dy[k]

                    if (0 <= new_x < m) and (0 <= new_y < n) and (visited[new_x][new_y] == 0):
                        if this_matrix[new_x][new_y] == 0:
                            return cur_index + 1

                        visited[new_x][new_y] = 1
                        q.put((new_x, new_y, cur_index + 1))

        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # print(i, j)
                    ans[i][j] = helper(i, j, matrix)
                    # print(ans[i][j])
                    # print('#' * 10)


        return ans
    """

    # 把矩阵看成一张图
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        from queue import Queue
        q = Queue()
        visted = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.put((i, j, 1))
                    visted[i][j] = 1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while not q.empty():
            cur = q.get()
            cur_x, cur_y, cur_index = cur[0], cur[1], cur[2]

            for k in range(4):
                new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                if (0 <= new_x < m) and (0 <= new_y < n) and (visted[new_x][new_y] == 0):
                    q.put((new_x, new_y, cur_index + 1))
                    matrix[new_x][new_y] = matrix[cur_x][cur_y] + 1
                    visted[new_x][new_y] = 1

        # print(matrix)
        return matrix
    """


if __name__ == '__main__':
    matrix1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    matrix2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    ans = Solution().updateMatrix(matrix2)
    print('ans: ', ans)
