# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 数组中只有一个重复数字, 那么坐标i应该与nums[i]元素相同, 如果不同则进行交换
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        nums = [num - 1 for num in nums]

        ans = set()
        for i in range(nums_len):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    if nums[i] not in ans:
                        ans.add(nums[i])
                    break

                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        ans = [val + 1 for val in ans]
        return ans


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    ans = Solution().findDuplicates(nums)
    print(ans)
