# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.c_list = ['a', 'b', 'c', 'x', 'y', 'z']

    def check(self, s):
        for c in self.c_list:
            c_count = s.count(c)
            # print(c, c_count)
            if c_count % 2 == 0:
                continue
            else:
                return False

        return True

    def solve(self, s):
        if not s: return 0
        s_len = len(s)

        ans = 0
        for i in range(s_len):
            c_count = {'a': 0, 'b': 0, 'c': 0, 'x': 0, 'y': 0, 'z': 0}
            for j in range(i, s_len):
                cc = s[j]
                if cc in c_count:
                    c_count[cc] += 1

                flag = True
                for cc in self.c_list:
                    if c_count[cc] % 2 != 0:
                        flag = False
                if flag:
                    ans = max(ans, j - i + 1)
        return ans


if __name__ == '__main__':
    s = input()
    ans = Solution().solve(s)
    print(ans)