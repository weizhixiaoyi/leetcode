# -*- coding:utf-8 -*-

#
# 翻译组合数
# @param num int整型 数字加密报文
# @return int整型
#
class Solution:
    def translateNum(self, num):
        # write code here
        num_str = '#' + str(num)
        num_len = len(num_str)
        dp = [0 for i in range(num_len)]
        dp[0] = 1
        dp[1] = 1
        # print(num_str, dp)

        for i in range(2, num_len):
            if num_str[i - 1] == '0':
                dp[i] = dp[i - 1]
                continue
            if '10' <= num_str[i - 1: i + 1] <= '25':
                dp[i] = dp[i - 1] + dp[i - 2]
                continue
            dp[i] = dp[i - 1]
        # print(dp)
        return dp[num_len - 1]


if __name__ == '__main__':
    num = 12158
    # num = int(input())
    ans = Solution().translateNum(num)
    print(ans)
