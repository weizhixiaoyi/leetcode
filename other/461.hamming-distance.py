# -*- coding:utf-8 -*-


class Solution:
    def binary(self, x: int) -> list:
        b = []
        while x != 0:
            if x % 2 == 0:
                b.append(0)
                x = x // 2
            else:
                b.append(1)
                x = x // 2
        b.reverse()
        return b

    def hammingDistance(self, x: int, y: int) -> int:
        bx = self.binary(x)
        by = self.binary(y)
        if len(bx) > len(by):
            m = len(bx) - len(by)
            by = [0 for i in range(m)] + by
        else:
            m = len(by) - len(bx)
            bx = [0 for i in range(m)] + bx
        # print(bx, by)
        # print([0 if bx[i] == by[i] else 1 for i in range(len(bx))])
        ans = sum([0 if bx[i] == by[i] else 1 for i in range(len(bx))])
        return ans


if __name__ == '__main__':
    x, y = 7, 4
    solution = Solution()
    ans = solution.hammingDistance(x, y)
    print('ans: ', ans)
