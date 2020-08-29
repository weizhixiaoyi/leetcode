# -*- coding:utf-8 -*-


class Solution:
    def solve(self, nums, nums_len):
        self.value = 100000007
        # self.rev = 0
        self.ans = 0
        tmp = [0 for i in range(nums_len)]
        self.sort(0, nums_len - 1, nums, tmp)
        # print(nums)
        # print(self.rev)
        # print(self.ans)
        return self.ans

    def sort(self, left, right, nums, tmp):
        if left >= right: return
        mid = (left + right) // 2
        self.sort(left, mid, nums, tmp)
        self.sort(mid + 1, right, nums, tmp)
        self.merge(left, mid, right, nums, tmp)

    def merge(self, left, mid, right, nums, tmp):
        i, j, k = left, mid + 1, 0
        while i <= mid and j <= right:
            while i <= mid and nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
                k += 1
            while j <= right and nums[i] > nums[j]:
                for l in range(i - 1, left - 1, -1):
                    if l <= mid and j <= right and nums[l] < nums[j]:
                        self.ans += (l - left) % self.value

                tmp[k] = nums[j]
                j += 1
                k += 1
                # self.rev += (mid - i + 1)

        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = nums[j]
            j += 1
            k += 1
        nums[left: right + 1] = tmp[0: k]


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 5
    # nums = [3, 5, 2, 4, 1]
    ans = Solution().solve(nums, n)
    print(ans)
