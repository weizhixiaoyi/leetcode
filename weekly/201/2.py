# -*- coding:utf-8 -*-

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev_inv(x):
            x_rev_inv = ''
            x_len = len(x)
            for i in range(x_len - 1, -1, -1):
                if x[i] == '0':
                    x_rev_inv += '1'
                else:
                    x_rev_inv += '0'
            return x_rev_inv

        cur_s = '0'
        for i in range(1, n):
            cur_s = cur_s + '1' + rev_inv(cur_s)
            # print(cur_s)
        return cur_s[k - 1]


if __name__ == '__main__':
    n, k = 3, 1
    # n, k = 4, 11
    ans = Solution().findKthBit(n, k)
    print(ans)
