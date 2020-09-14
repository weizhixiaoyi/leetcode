# -*- coding:utf-8 -*-

class Solution:
    def solve(self, line1, line2, line3, line4):
        x, y, z = line1
        a, b, c = line2
        machines_len = line3[0]
        machines = sorted(line4, reverse=True)

        def check(mid, machines):
            a_count, b_count, c_count = mid, mid, mid
            while True:
                pass

        from copy import deepcopy
        left, right = 0, 101
        while left < right:
            mid = (left + right + 1) // 2

            if check(mid, deepcopy(machines)):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line3 = list(map(int, input().split()))
    line4 = list(map(int, input().split()))
    ans = Solution().solve(line1, line2, line3, line4)
    print(ans)
