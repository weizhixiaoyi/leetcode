# -*- coding:utf-8 -*-

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        all_value = math.factorial(n)
        nums = [i + 1 for i in range(n)]
        if k > all_value // 2:
            nums = nums[::-1]
            k = all_value - k + 1

        self.cur_k, self.ans = 0, ''

        def dfs(path):
            if self.cur_k > k:
                return
            if len(path) == n:
                self.cur_k += 1
                if self.cur_k == k:
                    self.ans = path
                return

            for num in nums:
                if num in path: continue
                dfs(path + [num])

        dfs([])
        self.ans = [str(v) for v in self.ans]
        return ''.join(self.ans)


if __name__ == '__main__':
    n = 3
    k = 6
    ans = Solution().getPermutation(n, k)
    print(ans)
