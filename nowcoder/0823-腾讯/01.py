# -*- coding:utf-8 -*-


def solve(s):
    stack1 = []
    s_len = len(s)
    ans = 0
    for i in range(s_len):
        if s[i] == '(':
            stack1.append('(')
        if s[i] == '[':
            stack1.append('[')
        if s[i] == ')':
            if not stack1:
                ans += 1
            elif stack1[-1] != '(':
                ans += 1
                stack1.pop()
            else:
                stack1.pop()
        if s[i] == ']':
            if not stack1:
                ans += 1
            elif stack1[-1] != '[':
                ans += 1
                stack1.pop()
            else:
                stack1.pop()

        # print(i, stack1, ans)
    # print(stack1)
    if stack1:
        return ans + 1
    else:
        return ans


if __name__ == '__main__':
    # s = "[])"
    # s = ")(][][)("
    # s = ")([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]"
    s = input()
    ans = solve(s)
    print(ans)
