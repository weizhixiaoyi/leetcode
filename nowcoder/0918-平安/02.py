# -*- coding:utf-8 -*-

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param p float浮点型一维数组 第一个概率分布
# @param q float浮点型一维数组 四二个概率分布
# @return float浮点型
#
class Solution:
    def cross_entropy(self, p, q):
        # write code here
        import math
        nums_len = len(p)
        sum = 0

        hq = 0
        for i in range(nums_len):
            cur = -q[i] * math.log10(q[i])
            hq += cur
        hq = hq / 3

        hpq = 0
        for i in range(nums_len):
            cur = -p[i] * math.log10(hq)
            hpq += cur
        hpq = hpq / 3
        return hpq


if __name__ == '__main__':
    p = [0, 0.5, 0.5]
    q = [0.2, 0.2, 0.6]

    # nums = input().split('],[')
    # p, q = nums
    # p = p.replace('[', '')
    # q = q.replace(']', '')
    # p = p.split(',')
    # q = q.split(',')
    # p = list(map(float, p))
    # q = list(map(float, q))
    ans = Solution().cross_entropy(p, q)
    print(ans)
