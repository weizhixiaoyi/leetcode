# -*- coding:utf-8 -*-

def solve(nums_len, nums):
    nums_sorted = sorted(nums)
    min1, max1, max2 = nums[0], nums[-1], nums[-2]
    if max1 >= min1 + max2: return "NO"

    half_len = nums_len // 2
    new_nums = []
    left = nums_sorted[:half_len]
    right = nums_sorted[half_len:]
    if nums_len % 2 == 0:
        for i in range(0, half_len):
            new_nums.append(left[i])
            new_nums.append(right[i])
    else:
        new_nums.append(right[-1])
        for i in range(0, half_len):
            new_nums.append(left[i])
            new_nums.append(right[i])

    flag = False
    for k in range(0, nums_len - 2):
        if new_nums[k] >= new_nums[k + 1] + new_nums[k + 2]:
            flag = True
    if new_nums[nums_len - 2] >= new_nums[nums_len - 1] + new_nums[0]: flag = True
    if new_nums[nums_len - 1] >= new_nums[0] + new_nums[1]: flag = True
    if flag:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    # t = 1
    t = int(input())
    for i in range(t):
        # n = 5
        # nums = [17, 6, 17, 11, 17]
        n = int(input())
        nums = list(map(int, input().split()))
        ans = solve(n, nums)
        print(ans)
