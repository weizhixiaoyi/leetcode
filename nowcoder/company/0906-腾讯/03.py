# -*- coding:utf-8 -*-


class Solution:
    def solve(self, l, d):
        if l <= d:
            return '0.0000'
        else:
            return '1.0000'


if __name__ == '__main__':
    l, d = map(int, input().split())
    ans = Solution().solve(l, d)
    print(ans)
