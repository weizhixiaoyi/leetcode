# -*- coding:utf-8 -*-

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        n_sort = ''.join(sorted(n))
        if n == n_sort: return -1

        zero_count = 0
        for c in n_sort:
            if c == '0':
                zero_count += 1
        return int(n_sort[zero_count:] + n_sort[:zero_count])


if __name__ == '__main__':
    # n = 124300
    # n = 21
    n = 1
    ans = Solution().nextGreaterElement(n)
    print(ans)
