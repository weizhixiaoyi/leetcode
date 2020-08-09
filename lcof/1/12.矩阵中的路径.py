# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def helper(cur_x, cur_y, word, flag):
            if len(word) == 0:
                return True

            for k in range(4):
                new_x = cur_x + dx[k]
                new_y = cur_y + dy[k]

                # print(new_x, new_y)
                if (0 <= new_x < m) and (0 <= new_y < n) and (flag[new_x][new_y] is False) and (
                        board[new_x][new_y] == word[0]):
                    # print(new_x, new_y)
                    flag[new_x][new_y] = True
                    if helper(new_x, new_y, word[1:], flag):
                        return True
                    flag[new_x][new_y] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and len(word) == 1:
                    return True
                if board[i][j] == word[0]:
                    flag = [[False for j in range(n)] for i in range(m)]
                    flag[i][j] = True
                    ans = helper(i, j, word[1:], flag)
                    # print(i, j, ans)
                    # print('***' * 10)
                    if ans is True:
                        return True
        return False


if __name__ == '__main__':
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    board = [["a", "b"], ["c", "d"]]
    word = "abcd"
    # board = [['a', 'a']]
    # word = 'aaa'
    ans = Solution().exist(board, word)
    print(ans)
