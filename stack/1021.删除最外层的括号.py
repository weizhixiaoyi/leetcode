# -*- coding:utf-8 -*-

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if not s: return ''
        s_len = len(s)
        left = 0
        stack, cur_stack = [], []
        for i in range(s_len):
            if s[i] == '(':
                cur_stack.append('(')
            if s[i] == ')':
                cur_stack.pop()
            if not cur_stack:
                stack.append(s[left: i + 1])
                left = i + 1
        ans = []
        for i in range(len(stack)):
            cur_stack = stack[i]
            cur_stack_len = len(cur_stack)
            ans.append(cur_stack[1:-1])
        # print(ans)
        return ''.join(ans)


if __name__ == '__main__':
    # s = "(()())(())(()(()))"
    # s = "()()"
    s = "(()())(())"
    ans = Solution().removeOuterParentheses(s)
    print(ans)
