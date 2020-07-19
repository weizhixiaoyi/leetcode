# -*- coding:utf-8 -*-

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1. 确定num所在的位数
        start, digit, count = 1, 1, 9
        while n > count:
            n -= count

            start *= 10
            digit += 1
            count = 9 * start * digit
        # print(n, start, digit)

        # 2. 确定num所在的数组; n-1是需要去除开始数组
        num = start + (n - 1) // digit
        # print(num)

        # 3. 确定n在num中具体的位数
        ans = str(num)[(n - 1) % digit]
        return int(ans)


if __name__ == '__main__':
    n = 3
    ans = Solution().findNthDigit(n)
    print(ans)
