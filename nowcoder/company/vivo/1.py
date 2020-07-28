# -*- coding:utf-8 -*-

"""
给花园地的长度和一个0与1的数字序列。1表示种了花，0表示空地。花和花之间需要有一个空格才能栽种。输出能够种的花的数量。
例如
5
1 0 0 0 0
返回是2
"""
if __name__ == '__main__':
    n = int(input())
    temp = input().split(' ')
    temp1 = ''.join(temp)
    # print(temp1)
    temp2 = temp1.split('1')
    nums = []
    for i in range(0, len(temp2)):
        if temp2[i] == '':
            continue
        nums.append(temp2[i])

    nums_len = len(nums)
    ans = 0
    for i in range(0, nums_len):
        cur_val = nums[i]
        cur_val_len = len(nums[i])
        if i > 0 and i < nums_len - 1:
            if cur_val_len == 2:
                continue
            if cur_val_len == 1:
                continue
            if cur_val_len % 2 == 0:
                ans += (cur_val_len - 2) // 2
            else:
                ans += (cur_val_len - 1) // 2
        if i == 0:
            if cur_val_len == 1:
                continue
            if cur_val_len % 2 == 0:
                ans += (cur_val_len) // 2
            else:
                ans += (cur_val_len - 1) // 2
            continue
        if i == nums_len - 1:
            if cur_val_len == 1:
                continue
            if cur_val_len % 2 == 0:
                ans += (cur_val_len) // 2
            else:
                ans += (cur_val_len - 1) // 2
    print(ans)
