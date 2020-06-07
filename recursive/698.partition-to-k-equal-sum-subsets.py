# -*- coding:utf-8 -*-

from typing import List


# 针对递归, 重点还是要放在递归过程, 可从栈的过程去理解
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        if mod != 0: return False

        # 主要过程: 尝试去搜索数据, sum + cur_val如果和target相等, 则标记used[i] = True
        def search(k, cur_sum, index, used):
            # 当k==1时, 数组里无负数, 那么一定会满足条件
            if k == 1: return True

            # 如果找到一个结果, 那么待寻找个数为k-1, 重置条件继续寻找
            if cur_sum == target:
                print(index, nums[index], 'cur_sum == target')
                return search(k - 1, 0, 0, used)

            # 寻找满足数组的集合
            for i in range(index, len(nums)):
                print(index, cur_sum, 'cur_sum')
                if (cur_sum + nums[i] <= target) and (used[i] is False):
                    used[i] = True
                    print(i, nums[i], 'used[i] = True')
                    # 如果找到一个满足的答案, 则进行返回, 此处和k == 1时 return true相对应
                    # 如果相等的时候, 则不再会执行used[i] = False, 说明此数据已经利用
                    # 如果不想等, 则元素会进行出栈, 执行used[i] = False过程
                    if search(k, cur_sum + nums[i], i, used): return True
                    # 不满足条件进行回溯 used[i] = False, 即不加当前元素
                    used[i] = False
                    print(i, nums[i], 'used[i] = False')
                    print(used)

            print(index, nums[index], 'return False')
            print(used)
            return False

        nums.sort()
        while nums[-1] == target:
            nums.pop()
            k -= 1

        used = [False] * len(nums)
        return search(k, 0, 0, used)


if __name__ == '__main__':
    nums, k = [4, 3, 2, 3, 5, 2, 1], 4
    solution = Solution()
    ans = solution.canPartitionKSubsets(nums, k)
    print(ans)
