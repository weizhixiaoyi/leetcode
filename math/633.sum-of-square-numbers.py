# -*- coding:utf-8 -*-

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        num_max = int(math.sqrt(c)) + 1
        left, right = 0, num_max
        while left <= right:
            cur = left ** 2 + right ** 2
            if cur == c:
                return True
            if cur < c:
                left += 1
            if cur > c:
                right -= 1
        return False



if __name__ == '__main__':
    c = 2
    ans = Solution().judgeSquareSum(c)
    print('ans: ', ans)
