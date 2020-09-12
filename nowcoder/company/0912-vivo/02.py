# -*- coding:utf-8 -*-


class Solution:
    def isPar(self, s):
        s_len = len(s)
        if s_len % 2 == 0:
            left, right = s_len // 2 - 1, s_len // 2
        else:
            left, right = s_len // 2, s_len // 2
        while left >= 0 and right < s_len and s[left] == s[right]:
            left -= 1
            right += 1
        # print(left, right)
        if left == -1 and right == s_len:
            return True
        else:
            return False

    def solve(self, s):
        if not s: return 'false'
        # if self.isPar(s): return s
        s_len = len(s)

        for i in range(s_len):
            cur_s = s[:i] + s[i + 1:]
            # print(cur_s, self.isPar(cur_s))
            if self.isPar(cur_s):
                return cur_s

        return 'false'


if __name__ == '__main__':
    s = input()
    ans = Solution().solve(s)
    print(ans)

    # s = 'abca'
    # ans = Solution().isPar(s)
    # print(ans)
