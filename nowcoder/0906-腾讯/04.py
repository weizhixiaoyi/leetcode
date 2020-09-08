# -*- coding:utf-8 -*-


if __name__ == '__main__':
    t = int(input())
    for k in range(t):
        n = int(input())
        nums_dict = {}
        flag = False
        for i in range(n):
            line_nums = list(map(str, input().split()))
            min_value_idx = line_nums.index(min(line_nums))
            line_nums = line_nums[min_value_idx:] + line_nums[:min_value_idx]
            line_nums_str = ','.join(line_nums)
            if line_nums_str in nums_dict:
                flag = True
                break
            else:
                nums_dict[line_nums_str] = 1
        if flag:
            print('YES')
        else:
            print('NO')
