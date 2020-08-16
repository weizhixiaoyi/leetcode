# -*- coding:utf-8 -*-


def solve(nums1, nums2):
    nums1_len, nums2_len = len(nums1), len(nums2)
    idx = (nums1_len + nums2_len + 1) // 2 - 1
    i, j, k = 0, 0, 0
    while i < nums1_len and j < nums2_len:
        if nums1[i] < nums2[j]:
            if k == idx:
                return nums1[i]
            i += 1
            k += 1
        else:
            if k == idx:
                return nums2[j]
            j += 1
            k += 1
    while i < nums1_len:
        if k == idx:
            return nums1[i]
        i += 1
        k += 1
    while j < nums2_len:
        if k == idx:
            return nums2[j]
        j += 1
        k += 1


if __name__ == '__main__':
    # nums1 = [300, 500, 650, 700]
    # nums2 = [200, 275, 330]
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    ans = solve(nums1, nums2)
    print(ans)
