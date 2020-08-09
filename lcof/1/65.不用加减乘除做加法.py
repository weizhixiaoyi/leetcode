# -*- coding:utf-8 -*-

class Solution:
    def add(self, a: int, b: int) -> int:
        print(a & b)
        print((a & b) << 1)


if __name__ == '__main__':
    a, b = 3, 4
    ans = Solution().add(a, b)
    print(ans)
