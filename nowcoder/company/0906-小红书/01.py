# -*- coding:utf-8 -*-


class Solution:
    def solve(self, line):
        if not line: return 0
        line_len = len(line)
        stack = []
        ans = 0
        for i in range(line_len):
            if line[i].isdigit():
                cur = int(line[i])
                ans += cur
                stack.append(cur)
            if line[i] == '+':
                if len(stack) < 2: continue
                cur = stack[-1] + stack[-2]
                ans += cur
                stack.append(cur)
            if line[i] == '-':
                if len(stack) < 2: continue
                cur = abs(stack[-1] - stack[-2])
                ans += cur
                stack.append(cur)
            if line[i] == 'T':
                if not stack: continue
                cur = stack[-1] * 3
                ans += cur
                stack.append(cur)
            if line[i] == 'C':
                if not stack: continue
                cur = stack.pop()
                ans -= cur
            # print(stack)
            # print(ans)

        return ans


if __name__ == '__main__':
    line = input().split()
    ans = Solution().solve(line)
    print(ans)
