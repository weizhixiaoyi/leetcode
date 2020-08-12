# -*- coding:utf-8 -*-
from typing import List
import pprint


class Solution:
    """
    def solve(self, board: List[List[str]]) -> None:
        if not board: return

        def helper(start_x, start_y):
            from queue import Queue
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            ok = True
            tmp = []
            q = Queue()
            q.put((start_x, start_y))
            flag[start_x][start_y] = False

            while not q.empty():
                cur = q.get()
                cur_x, cur_y = cur[0], cur[1]
                tmp.append((cur_x, cur_y))
                for k in range(4):
                    new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                    if board[new_x][new_y] == 'X': continue
                    if board[new_x][new_y] == 'O' and (new_x == 0 or new_x == m - 1 or new_y == 0 or new_y == n - 1):
                        ok = False
                        q.queue.clear()
                        tmp = []
                        break
                    elif board[new_x][new_y] == 'O' and flag[new_x][new_y] is True:
                        flag[new_x][new_y] = False
                        q.put((new_x, new_y))

            return ok, tmp

        m, n = len(board), len(board[0])
        flag = [[True for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X': flag[i][j] = False
                if (i == 0) or (j == 0) or (i == m - 1) or (j == n - 1): flag[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' or not flag[i][j]: continue
                pre_flag = flag
                ok, tmp = helper(i, j)
                if ok:
                    for cur in tmp:
                        cur_x, cur_y = cur[0], cur[1]
                        board[cur_x][cur_y] = 'X'
                        flag[cur_x][cur_y] = False
                if not ok:
                    flag = pre_flag

        # ans = []
        # for line in board:
        #     ans.append([''.join(line)])
        # pprint.pprint(ans)
    """

    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m, n = len(board), len(board[0])

        def helper(start_x, start_y):
            if start_x < 0 or start_x >= m or start_y < 0 or start_y >= n or board[start_x][start_y] != 'O':
                return
            board[start_x][start_y] = 'A'
            helper(start_x + 1, start_y)
            helper(start_x - 1, start_y)
            helper(start_x, start_y + 1)
            helper(start_x, start_y - 1)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    helper(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        # print(board)


if __name__ == '__main__':
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    # board = [["O", "X", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
    #          ["O", "X", "O", "X", "O", "O", "O", "O", "X"], ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
    #          ["X", "O", "O", "O", "O", "O", "O", "O", "X"], ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
    #          ["O", "O", "O", "X", "O", "O", "O", "O", "O"], ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    #          ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]
    Solution().solve(board)
