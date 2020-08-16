# -*- coding:utf-8 -*-


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        if n % 2 == 1:
            mid = n // 2
            ans = mid * (mid + 1)
        else:
            k = 1
            while k < n:
                ans += k
                k += 2

        return ans


if __name__ == '__main__':
    n = 2
    ans = Solution().minOperations(n)
    print(ans)
