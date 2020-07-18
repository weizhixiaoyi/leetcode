# -*- coding:utf-8 -*-
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        num_len = len(num)
        if num_len == 1: return 1

        dp = [0 for i in range(num_len + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, num_len + 1):
            if '10' <= num[i - 2: i] < '26':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        # print(dp)
        return dp[num_len]


if __name__ == '__main__':
    # num = 18580
    num = 12258
    ans = Solution().translateNum(num)
    print(ans)
