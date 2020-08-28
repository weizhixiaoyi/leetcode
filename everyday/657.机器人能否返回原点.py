# -*- coding:utf-8 -*-

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves: return True

        x, y = 0, 0
        for c in moves:
            if c == 'U': x -= 1
            if c == 'D': x += 1
            if c == 'R': y += 1
            if c == 'L': y -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    moves = "UD"
    ans = Solution().judgeCircle(moves)
    print(ans)
