# -*- coding:utf-8 -*-

class Solution:
    def solveEquation(self, equation: str) -> str:
        equation_split = equation.split('=')
        if len(equation_split) == 0: return "No solution"
        left_s, right_s = equation_split[0], equation_split[1]
        # 将'-'替换为'+-'方便分割处理
        left_l, right_l = left_s.replace('-', '+-').split('+'), right_s.replace('-', '+-').split('+')
        left_l, right_l = [x for x in left_l if x != ""], [x for x in right_l if x != ""]
        # print(left_l, right_l)

        left_x, right_x = 0, 0
        left_val, right_val = 0, 0
        for x in left_l:
            if x[0] == '-' and x[-1] == 'x':
                if x[1].isdigit():
                    left_x -= int(x[1:-1])
                else:
                    left_x -= 1
                continue
            if x[-1] == 'x':
                if x[0].isdigit():
                    left_x += int(x[0:-1])
                else:
                    left_x += 1
                continue

            left_val += int(x)

        # print(left_x, left_val)
        for x in right_l:
            if x[0] == '-' and x[-1] == 'x':
                if x[1].isdigit():
                    right_x -= int(x[1:-1])
                else:
                    right_x -= 1
                continue
            if x[-1] == 'x':
                if x[0].isdigit():
                    right_x += int(x[0:-1])
                else:
                    right_x += 1
                continue

            right_val += int(x)

        # print(left_x, right_x)
        # print(left_val, right_val)
        num_x = left_x - right_x
        num_val = right_val - left_val
        # print(num_x, num_val)

        if num_x == 0 and num_val != 0: return "No solution"
        if num_x == 0 and num_val == 0: return "Infinite solutions"
        if num_x != 0:
            return "x=" + str(num_val // num_x)


if __name__ == '__main__':
    equation = "-99x=99"
    ans = Solution().solveEquation(equation)
    print('ans: ', ans)
