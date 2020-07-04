# -*- coding:utf-8 -*-

class Solution:
    # O(n**2)解决问题
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     s_len = len(s)
    #     if s_len == 0: return 0
    #     if s_len == 1: return 1
    #
    #     ans = 0
    #     for i in range(0, s_len):
    #         cur_set = set()
    #         cur_ans = 0
    #         for j in range(i, s_len):
    #             if s[j] in cur_set:
    #                 break
    #             cur_set.add(s[j])
    #             cur_ans += 1
    #         ans = max(cur_ans, ans)
    #     # print(ans)
    #     return ans

    # 滑动窗口O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0: return 0
        if s_len == 1: return 1

        # 滑动窗口
        s_set, k, ans = set(), -1, 0
        for i in range(0, s_len):
            if i != 0:
                s_set.remove(s[i - 1])
            while k + 1 < s_len and s[k + 1] not in s_set:
                s_set.add(s[k + 1])
                k += 1
            ans = max(ans, k - i + 1)
        return ans


if __name__ == '__main__':
    s = "bbcbb"
    ans = Solution().lengthOfLongestSubstring(s)
    print('ans: ', ans)
