# -*- coding:utf-8 -*-


def solve(nums, nums_len):
    idx = 0
    while True:
        pre_nums = nums
        # 尽可能的消除

        need_remove = []
        left_value = nums[0]
        cur_nums_len = len(nums)
        for i in range(1, cur_nums_len):
            if nums[i] < left_value and nums[i] < nums[i - 1]:
                need_remove.append(i)
            else:
                left_value = nums[i]

        tmp_nums = []
        for i in range(cur_nums_len):
            if i in need_remove:
                continue
            else:
                tmp_nums.append(nums[i])
        # print(tmp_nums)
        nums = tmp_nums

        if pre_nums == nums:
            return idx
        else:
            idx += 1


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    ans = solve(nums, n)
    print(ans)
