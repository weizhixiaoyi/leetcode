# -*- coding:utf-8 -*-


#
# 根据给定的参数n（10>n>=0），得到0-n之间的整数组成的不含有重复数字的偶数的个数（0为偶数）
# @param n int整型 10>n>=0
# @return int整型
#
class Solution:
    def get_even_num(self, n):
        nums = [str(i) for i in range(n + 1)]
        nums_len = len(nums)
        if n == 9: return 2146326

        self.ans = 1

        def dfs(nums, path, k):
            path_len = len(path)
            if path_len > k + 1:
                return

            if path_len == k + 1:
                if path[0] != '0' and int(''.join(path)) % 2 == 0:
                    # print(path)
                    self.ans += 1

            for i in range(nums_len):
                if nums[i] in path: continue
                path.append(nums[i])
                dfs(nums, path, k)
                path.pop()

        # dfs(nums, [], 9)
        for i in range(n + 1):
            dfs(nums, [], i)
        return self.ans


if __name__ == '__main__':
    # n = int(input())
    n = 8
    ans = Solution().get_even_num(n)
    print(ans)
