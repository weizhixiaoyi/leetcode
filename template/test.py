# -*- coding:utf-8 -*-

def solve(nums):
    if len(nums) == 0:
        return 0

    left = nums[0] - solve(nums[1:])
    right = nums[-1] - solve(nums[0:-1])

    return max(left, right)


if __name__ == '__main__':
    # nums = [1, 5, 2]
    nums = [1, 5, 233, 7]
    ans = solve(nums)
    print(ans)
