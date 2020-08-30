# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from operator import truediv
        tokens_len = len(tokens)
        stack = []

        for i in range(tokens_len):
            token = tokens[i]
            if token.startswith('-') and token[1:].isdigit() or token.isdigit():
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = 0
                if token == '+':
                    val3 = val2 + val1
                elif token == '-':
                    val3 = val2 - val1
                elif token == '*':
                    val3 = val2 * val1
                elif token == '/':
                    # val3 = int(truediv(val2, val1))
                    val3 = int(val2 / val1)
                stack.append(val3)
                # print(val2, token, val1, '=', val3)

        ans = int(stack[0])
        return ans


if __name__ == '__main__':
    # tokens = ["2", "1", "+", "3", "*"]
    # tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ans = Solution().evalRPN(tokens)
    print(ans)
