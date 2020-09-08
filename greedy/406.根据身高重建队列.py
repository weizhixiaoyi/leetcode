# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_len = len(people)
        used = [0 for i in range(people_len)]

        people = sorted(people, key=lambda d: (d[1], d[0]))
        ans = []
        for i in range(people_len):
            if i == 0:
                ans.append(people[i])
                used[i] = 1
            else:
                cur_height = [v[0] for v in ans]
                cur_height = sorted(cur_height)
                cur_height_len = len(cur_height)
                min_value, min_index = float('inf'), 0

                for j in range(people_len):
                    if used[j]: continue
                    # 判断当前是否符合, 符合情况下选取最小元素
                    cur_h, cur_k = people[j][0], people[j][1]
                    count_k = self.binary_search(cur_height, cur_height_len, cur_h)
                    if count_k == cur_k and cur_h < min_value:
                        min_value = cur_h
                        min_index = j
                ans.append(people[min_index])
                used[min_index] = 1
        return ans

    def binary_search(self, nums, nums_len, target):
        left, right = 0, nums_len
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return nums_len - left


if __name__ == '__main__':
    # people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    ans = Solution().reconstructQueue(people)
    print(ans)
