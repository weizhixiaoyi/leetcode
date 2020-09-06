# -*- coding:utf-8 -*-


class Solution:
    def solve(self, nums, nums_len):
        nums = sorted(nums)
        if nums_len % 2 == 0:
            return "NO"
        else:
            from collections import defaultdict
            ans_dict = defaultdict(list)
            ans_dict[1] = [1]
            ans_dict[3] = [1, 1, 3]
            ans_dict[5] = [1, 1, 1, 3, 5]
            ans_dict[7] = [1, 1, 1, 1, 3, 3, 7]
            ans_dict[9] = [1, 1, 1, 1, 1, 3, 3, 5, 9]
            ans_dict[11] = [1, 1, 1, 1, 1, 1, 3, 3, 3, 7, 11]
            ans_dict[13] = [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 5, 7, 13]
            ans_dict[15] = [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 7, 7, 15]
            ans_dict[17] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 5, 7, 9, 17]
            ans_dict[19] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 7, 7, 11, 19]
            ans_dict[21] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 7, 7, 13, 21]
            ans_dict[23] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 7, 7, 7, 15, 23]
            # print(ans_dict)
            if nums == ans_dict[nums_len]:
                return "YES"
            else:
                return "NO"


if __name__ == '__main__':
    # test = True
    test = False
    if test is True:
        n = 3
        nums = [1, 1, 3]
        # n = int(input())
        # nums = list(map(int, input().split()))
        ans = Solution().solve(nums, n)
        print(ans)
    else:
        while True:
            try:
                n = int(input())
                nums = list(map(int, input().split()))
                ans = Solution().solve(nums, n)
                print(ans)
            except:
                break
