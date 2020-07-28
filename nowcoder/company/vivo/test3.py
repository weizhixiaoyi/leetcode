# -*- coding:utf-8 -*-

# problem link: https://www.nowcoder.com/question/next?pid=22390442&qid=925106&tid=33906960
# @param n int整型 第n天
# @return int整型

class Solution:
    def solution(self, n):
        # write code here
        dp1 = [i for i in range(100)]
        dp2 = [((1 + dp1[i]) * dp1[i]) // 2 for i in range(100)]

        index = 0
        for k in range(1, len(dp2)):
            if (n >= dp2[k - 1] and n < dp2[k]) or (n > dp2[k - 1] and n <= dp2[k]):
                index = k
                break

        if dp2[index] == n:
            return sum([dp1[i] ** 2 for i in range(1, index + 1)])
        else:
            pre, now = index - 1, index
            ans = sum([dp1[i] ** 2 for i in range(1, pre + 1)])
            ans += (n - dp2[pre]) * dp1[now]
            return ans


if __name__ == '__main__':
    while True:
        n = int(input())
        s = Solution()
        ans = s.solution(n)
        print(ans)
