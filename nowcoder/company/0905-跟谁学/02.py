# -*- coding:utf-8 -*-

import random


class Solution:
    def solve(self, n):
        # 1代表男孩, 2代表女孩
        all_sum = 0
        for i in range(n):
            idx = 0
            boy, girl = False, False
            while True:
                idx += 1
                cur = self.get_random()
                if cur == 1:
                    boy = True
                if cur == 2:
                    girl = True
                if boy and girl:
                    break

            all_sum += idx
        average = all_sum // n
        return average

    def get_random(self):
        n = random.randint(1, 1000)
        if n % 2 == 0:
            return 1
        else:
            return 2


if __name__ == '__main__':
    n = 100000
    ans = Solution().solve(n)
    print(ans)
