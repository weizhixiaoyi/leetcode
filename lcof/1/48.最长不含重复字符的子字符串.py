# -*- coding:utf-8 -*-

class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s: return 0
    #
    #     s_len = len(s)
    #     cur_set = set()
    #     start, end, ans = 0, 0, 0
    #     while start < s_len:
    #         while (end < s_len) and (s[end] not in cur_set):
    #             cur_set.add(s[end])
    #             end += 1
    #
    #         ans = max(ans, len(cur_set))
    #
    #         cur_set.remove(s[start])
    #         start += 1
    #
    #     return ans

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s: return 0
    #
    #     cur_set = set()
    #     cur_len, max_len, s_len = 0, 0, len(s)
    #     start = 0
    #     for i in range(s_len):
    #         cur_len += 1
    #         while s[i] in cur_set:
    #             cur_set.remove(s[start])
    #             start += 1
    #             cur_len -= 1
    #
    #         if cur_len > max_len: max_len = cur_len
    #         cur_set.add(s[i])
    #
    #     return max_len

    # Hash
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        cur_dict = {}
        start, ans = 0, 0
        for i, c in enumerate(s):
            if (c in cur_dict) and (cur_dict[c] >= start):
                start = cur_dict[c] + 1
                cur_dict[c] = i
            else:
                cur_dict[c] = i
                ans = max(ans, i - start + 1)
                # print(i, c, ans)

        return ans


if __name__ == '__main__':
    # s = "pwwkew"
    s = "abcabcbb"
    ans = Solution().lengthOfLongestSubstring(s)
    print(ans)
