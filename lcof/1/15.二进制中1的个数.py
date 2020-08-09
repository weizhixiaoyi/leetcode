# -*- coding:utf-8 -*-

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2
                ans += 1

        return ans


if __name__ == '__main__':
    n = 9
    ans = Solution().hammingWeight(n)
    print(ans)
