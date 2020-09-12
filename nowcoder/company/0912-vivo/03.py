# -*- coding:utf-8 -*-


class Solution:
    def solve(self, s):
        s = list(map(int, s))
        s_len = len(s)
        ans = []
        from collections import defaultdict
        s_dict = defaultdict(list)
        for i in range(s_len):
            cur = s[i]
            if cur == -1:
                ans.append(i)
                continue
            s_dict[cur].append(i)

        while len(s_dict) != 0:
            for key, value in s_dict.items():
                if len(value) == 1:
                    ans.append(key)
                    s.pop(key)


if __name__ == '__main__':
    # s = input()
    # s = s.replace('\"', '')
    # s = s.split(',')
    s = [1, 2, -1, 1]
    ans = Solution().solve(s)
    print(ans)
