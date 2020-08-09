# -*- coding:utf-8 -*-

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


if __name__ == '__main__':
    s = "We%20are%20happy."
    ans = Solution().replaceSpace(s)
    print(ans)
