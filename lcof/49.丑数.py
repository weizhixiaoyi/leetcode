# -*- coding:utf-8 -*-

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # ans = [1]
        # for k in range(1, n + 1):
        #     pre = ans
        #     max_pre = max(pre)
        #     min_value = float('inf')
        #     for v in pre:
        #         v2, v3, v5 = v * 2, v * 3, v * 5
        #         if (v2 > max_pre) and (v2 < min_value):
        #             min_value = v2
        #         if (v3 > max_pre) and (v3 < min_value):
        #             min_value = v3
        #         if (v5 > max_pre) and (v5 < min_value):
        #             min_value = v5
        #     ans.append(min_value)
        # return ans[n - 1]

        ans = [0 for i in range(n + 1)]
        ans[0] = 1
        a, b, c = 0, 0, 0
        for k in range(1, n + 1):
            ans[k] = min([ans[a] * 2, ans[b] * 3, ans[c] * 5])
            if ans[a] * 2 == ans[k]:
                a += 1
            if ans[b] * 3 == ans[k]:
                b += 1
            if ans[c] * 5 == ans[k]:
                c += 1
        return ans[n - 1]


if __name__ == '__main__':
    n = 1690
    ans = Solution().nthUglyNumber(n)
    print(ans)
