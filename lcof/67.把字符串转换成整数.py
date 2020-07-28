# -*- coding:utf-8 -*-

class Solution:
    def strToInt(self, str) -> int:
        str = str.strip()
        if not str: return 0
        max_value = pow(2, 31) - 1
        min_value = -(max_value + 1)

        sign = 1
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]

        res = 0
        for c in str:
            if c > '9' or c < '0':
                break
            res *= 10
            res += int(c)
        # print(res)

        if sign == 1: return min(res, max_value)
        if sign == -1: return max(-res, min_value)
        return 0


if __name__ == '__main__':
    # str = "words and 987"
    # str = "4193 with words"
    # str = "-91283472332"
    # str = "  -0012a42"
    str = '+-0'
    ans = Solution().strToInt(str)
    print(ans)
