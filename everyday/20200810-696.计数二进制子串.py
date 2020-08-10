# -*- coding:utf-8 -*-

class Solution:
    """
    def countBinarySubstrings(self, s: str) -> int:
        s_len = len(s)
        self.ans = 0

        def helper(l, r):
            self.ans += 1
            while l - 1 >= 0 and r + 1 < s_len and s[l - 1] == s[l] and s[r + 1] == s[r]:
                l -= 1
                r += 1
                self.ans += 1

        for k in range(0, s_len - 1):
            if s[k: k + 2] == '01' or s[k: k + 2] == '10':
                helper(k, k + 1)

        return self.ans
    """

    # 复杂度O(n)
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        i, s_len = 0, len(s)
        while i < s_len:
            count = 0
            cur = s[i]
            while i < s_len and s[i] == cur:
                i += 1
                count += 1
            counts.append(count)
        # print(counts)

        counts_len = len(counts)
        ans = 0
        for k in range(0, counts_len - 1):
            ans += min(counts[k], counts[k + 1])
        return ans


if __name__ == '__main__':
    s = "00110011"
    # s = "10101"
    ans = Solution().countBinarySubstrings(s)
    print(ans)
