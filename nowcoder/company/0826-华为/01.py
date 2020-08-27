# -*- coding:utf-8 -*-


def solve(nums):
    nums_len = len(nums)
    nums_bin = []
    for num in nums:
        cur_bin = bin(num)[2:]
        cur_bin = list(cur_bin)
        cur_bin_len = len(cur_bin)
        cur_bin = (32 - cur_bin_len) * ['0'] + cur_bin
        nums_bin.append(cur_bin)
    # print(nums_bin)

    # swap
    for i in range(nums_len):
        cur_bin = nums_bin[i]
        for i in range(0, 32, 2):
            cur_bin[i], cur_bin[i + 1] = cur_bin[i + 1], cur_bin[i]
    # print(nums_bin)

    all_str = ''
    for i in range(nums_len):
        cur_str = ''.join(nums_bin[i])
        all_str += cur_str
    all_str = all_str[-2:] + all_str[:-2]
    # print(all_str)
    all_str_len = len(all_str)

    tmp_nums = []
    tmp_str = ''
    k = 0
    for i in range(all_str_len):
        tmp_str += all_str[i]
        k += 1
        if k == 32:
            tmp_nums.append(tmp_str)
            tmp_str = ''
            k = 0

    # 转换为整数
    # print(tmp_nums)
    ans_nums = []
    for n in tmp_nums:
        ans_nums.append(str(int(n, 2)))
    ans_nums = ' '.join(ans_nums)
    return ans_nums


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    # nums = [1, 2]
    ans = solve(nums)
    print(ans)