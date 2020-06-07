# -*- coding:utf-8 -*-


def binary_search(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = int((low + high) // 2)
        if nums[mid] == k:
            return mid
        if nums[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    nums, k = [1, 2, 3, 4, 5, 6, 7, 8, 9], 9
    ans = binary_search(nums, k)
    print(ans)
