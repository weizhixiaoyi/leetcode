# -*- coding:utf-8 -*-


# 如果答案在左区间, 并且mid也可能是答案
def binary_search1(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    # return left
    return left if nums[left] == target else -1


# 如果答案在右区间, 并且mid也可能是答案
def binary_serrch2(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right + 1) // 2
        print(left, mid, right)
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1

    # return left
    return left if nums[left] == target else -1


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 4, 4, 5, 6, 7]
    target = 3
    ans1 = binary_search1(nums, target)
    print(ans1, end='\n\n')

    ans2 = binary_serrch2(nums, target)
    print(ans2)
