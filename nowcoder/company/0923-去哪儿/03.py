# -*- coding:utf-8 -*-


class Solution:
    def solve(self, nums, nums_len):
        from collections import defaultdict
        color = defaultdict(int)
        pai = []
        for i in range(nums_len):
            c, p = nums[i][0], nums[i][1:]
            if p == 'J': p = '11'
            if p == 'Q': p = '12'
            if p == 'K': p = '13'
            if p == 'A': p = '14'
            pai.append(p)
            color[c] += 1

        max_diff = 0
        for key, value in color.items():
            max_diff = max(max_diff, value)
        if max_diff == 5:
            if '14' in pai:
                return "HuangJiaTongHuaShun"
            else:
                return "TongHuaShun"
        if max_diff == 4:
            return "SiTiao"
        if max_diff == 3:
            return "HuLu"
        if max_diff == 2:
            return "LiangDui"
        return "GaoPai"


if __name__ == '__main__':
    n = int(input())
    line = input().split()
    # n = 5
    # line = ["SA", "SK", "SQ", "SJ", "S10"]
    ans = Solution().solve(line, n)
    print(ans)
