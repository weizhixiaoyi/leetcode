# -*- coding:utf-8 -*-


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return ''
        s_len = len(s)

        remove = []
        stack = []
        for i in range(s_len):
            if s[i] == '(':
                stack.append('(')
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    remove.append(i)

        stack_len = len(stack)
        for i in range(s_len - 1, -1, -1):
            if stack_len and s[i] == '(':
                remove.append(i)
                stack_len -= 1

        ans = []
        for i in range(s_len):
            if i in remove:
                continue
            ans.append(s[i])
        ans = ''.join(ans)
        return ans


if __name__ == '__main__':
    # s = "lee(t(c)o)de)"
    # s = "(a(b(c)d)"
    # s = "a)b(c)d"
    s = "))(("
    ans = Solution().minRemoveToMakeValid(s)
    print(ans)
