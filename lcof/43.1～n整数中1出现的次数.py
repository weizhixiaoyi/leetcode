# -*- coding:utf-8 -*-

class Solution:
    def countDigitOne(self, n: int) -> int:
        for i in range(1, 101):
            print(i, end=' ')
            if i % 10 == 0:
                print()

        print()
        for i in range(100, 1001):
            print(i, end=' ')
            if i % 100 == 0:
                print()


if __name__ == '__main__':
    n = 12
    ans = Solution().countDigitOne(n)
    print(ans)
