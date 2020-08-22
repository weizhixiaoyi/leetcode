# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n, word_len = len(board), len(board[0]), len(word)

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        self.ans = False

        def dfs(cur_x, cur_y, idx):
            if idx == word_len:
                return True

            flag = False
            tmp = board[cur_x][cur_y]
            board[cur_x][cur_y] = '*'
            for k in range(4):
                new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or board[new_x][new_y] == '*': continue
                if board[new_x][new_y] == word[idx]:
                    flag = flag or dfs(new_x, new_y, idx + 1)
            board[cur_x][cur_y] = tmp
            return flag

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
                # if board[i][j] == word[0]:
                #     print(dfs(i, j, 1))
        return False


if __name__ == '__main__':
    # board = [
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']
    # ]
    # word = "ABCCED"
    board = [['a', 'a']]
    word = 'aaa'
    # board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    # word = 'AAB'
    ans = Solution().exist(board, word)
    print(ans)
