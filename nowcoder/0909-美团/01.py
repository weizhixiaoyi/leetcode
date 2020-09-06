# -*- coding:utf-8 -*-


class Solution:
    def solve(self, line1, line2, line3):
        n, p, q = line1
        line2_len = p
        line3_len = q

        # a想要
        line2_set = set(line2)
        line3_set = set(line3)
        ab_want = len(line2_set.intersection(line3_set))
        a_want = line2_len - ab_want
        b_want = line3_len - ab_want

        print(a_want, b_want, ab_want)


if __name__ == '__main__':
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line3 = list(map(int, input().split()))
    Solution().solve(line1, line2, line3)
