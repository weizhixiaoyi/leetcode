# -*- coding:utf-8 -*-


def solve(nums):
    nums = sorted(nums)
    l1, l4 = nums[0], nums[3]
    if l1 == l4:
        return sum(nums)
    while l1 != l4:
        diff = l4 - l1
        if diff >= 3:
            diff = diff // 3
            nums[3] = nums[3] - 2 * diff
            nums[0] = nums[0] + diff
        else:
            l3, l4 = nums[2], nums[3]
            if l3 > l1 and l4 > l1:
                nums[0] += 1
                nums[2] -= 1
                nums[3] -= 1
            else:
                return -1
        print(nums)

        nums = sorted(nums)
        l1, l4 = nums[0], nums[3]
        if l1 == l4:
            return sum(nums)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    ans = solve(nums)
    print(ans)
