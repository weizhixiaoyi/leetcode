# -*- coding:utf-8 -*-


class Solution:
    """
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        s_len = len(s)

        ans = 0
        for i in range(s_len - 1):
            for j in range(s_len - 1, i, -1):
                if self.isValid(s[i: j + 1]):
                    print(s[i: j + 1])
                    # return j - i + 1
                    ans = max(ans, j - i + 1)
        return ans

    def isValid(self, s):
        if not s: return False
        s_len = len(s)

        stack = []
        for i in range(s_len):
            if s[i] == '(':
                stack.append('(')
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
    """

    """
    def longestValidParentheses(self, s: str) -> int:
        # 合法的符号是顺序递增的
        if not s: return 0
        s_len = len(s)

        stack = []
        nums = []
        for i in range(s_len):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    nums.extend([stack.pop(), i])
        nums = sorted(nums)
        # print(nums)

        ans = 0
        tmp = []
        left = 0
        nums_len = len(nums)
        for i in range(nums_len):
            if tmp and (nums[i] - nums[left] + 1) != (i - left + 1):
                ans = max(ans, i - left)
                tmp = []
                left = i

            tmp.append(nums[i])
        # print(tmp)
        ans = max(ans, len(tmp))
        return ans
    """

    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        s_len = len(s)

        dp = [0 for i in range(s_len)]
        for i in range(s_len):
            if i > 0 and s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ')' and (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)


if __name__ == '__main__':
    # s = ")()())"
    # s = "(()"
    # s = ")(())))(())())"
    s = ')('
    ans = Solution().longestValidParentheses(s)
    print(ans)
