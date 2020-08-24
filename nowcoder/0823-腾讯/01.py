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

    if stack1:
        return ans + 1
    else:
        return ans


def solve1(s):
    s_len = len(s)
    dp = [[0 for j in range(s_len)] for i in range(s_len)]
    for i in range(s_len):
        dp[i][i] = 1

    for i in range(s_len):
        for j in range(i + 1):
            # 最多需要的数量: 针对已有的都再补一个
            dp[j][i] = dp[j][i - 1] + 1

            # 假设是以k进行分成两段, 左边已经完美匹配, 右边第k个为'(' 或'[', 右边第i个是')' 或']', 则类似（...)或者[...]
            # 最后表达为dp[j][i] = min(dp[j][i], dp[j][k - 1] + dp[k + 1][
            for k in range(j, i):
                if (s[k] == '(' and s[i] == ')') or (s[k] == '[' and s[i] == ']'):
                    dp[j][i] = min(dp[j][i], dp[j][k - 1] + dp[k + 1][i - 1])
    return dp[0][s_len - 1]


if __name__ == '__main__':
    s = "[])"
    # s = ")(][][)("
    # s = ")([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]"
    # s = input()
    ans = solve1(s)
    print(ans)
