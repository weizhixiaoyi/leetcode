# -*- coding:utf-8 -*-


def quickSort(nums, i, j):
    if i >= j: return []
    pivot = nums[i]
    low, high = i, j

    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]

        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]
    nums[i] = pivot

    quickSort(nums, low, i - 1)
    quickSort(nums, i + 1, high)
    return nums


if __name__ == '__main__':
    nums = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    # nums = [5, 4, 3, 2, 1]
    # nums = [1, 2, 3, 4]
    ans = quickSort(nums, 0, len(nums) - 1)
    print(ans)
