# -*- coding:utf-8 -*-


def solve(nums):
    A, B, a, b = nums[0], nums[1], nums[2], nums[3]
    if A <= B:
        idx = 0
        for x in range(A, 0, -1):
            if (x * b) % a == 0:
                cur_y = (x * b) // a
                if 1 <= cur_y <= B:
                    return x, cur_y
            idx += 1
            if idx > 8000000:
                return 0, 0
        return 0, 0
    else:
        idx = 0
        for y in range(B, 0, -1):
            if (y * a) % b == 0:
                cur_x = (a * y) // b
                if 1 <= cur_x <= A:
                    return cur_x, y
            idx += 1
            if idx > 8000000:
                return 0, 0
        return 0, 0


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    x, y = solve(nums)
    print(x, y)
