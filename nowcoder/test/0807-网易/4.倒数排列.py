# -*- coding:utf-8 -*-

def solve(nums_len, nums):
    map_dict = {}
    for num in nums:
        map_dict[num] = nums_len - num + 1
    # print(map_dict)

    ans = []
    for num in nums:
        ans.append(map_dict[num])

    ans = [str(val) for val in ans]
    return ' '.join(ans)


if __name__ == '__main__':
    # n = 5
    # nums = [3, 1, 5, 2, 4]
    # n = 3
    # nums = [1, 2, 3]
    # n = 4
    # nums = [1, 2, 3, 4]
    n = int(input())
    nums = list(map(int, input().split()))
    ans = solve(n, nums)
    print(ans)
