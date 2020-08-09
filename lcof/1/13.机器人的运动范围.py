# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        flag = [[1 for j in range(n)] for i in range(m)]

        def digit(n):
            ans = 0
            while n != 0:
                ans += (n % 10)
                n //= 10
            return ans

        for i in range(m):
            for j in range(n):
                value = digit(i) + digit(j)
                if value > k:
                    flag[i][j] = 0

        # print(flag)

        # could get
        def helper(i, j):
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            from queue import Queue
            q = Queue()
            q.put((i, j))
            flag[i][j] = 0
            cur_ans = 1

            while not q.empty():
                cur = q.get()
                cur_x, cur_y = cur[0], cur[1]
                for k in range(4):
                    new_x = cur_x + dx[k]
                    new_y = cur_y + dy[k]

                    if (0 <= new_x < m) and (0 <= new_y < n) and (flag[new_x][new_y] == 1):
                        flag[new_x][new_y] = 0
                        cur_ans += 1
                        q.put((new_x, new_y))

            return cur_ans

        return helper(0, 0)


if __name__ == '__main__':
    # m, n, k = 2, 3, 1
    # m, n, k = 3, 1, 0
    # m, n, k = 16, 8, 4
    ans = Solution().movingCount(m, n, k)
    print(ans)
