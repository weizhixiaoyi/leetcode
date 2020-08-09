# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        postorder_len = len(postorder)
        if postorder_len == 0: return True
        if postorder_len == 1: return True

        def helper(i, j):
            if i >= j: return True

            m = i
            for k in range(i, j + 1):
                if postorder[k] < postorder[j]:
                    m += 1
            n = m
            for k in range(n, j):
                if postorder[k] > postorder[j]:
                    n += 1

            left = helper(i, n - 1)
            right = helper(n, j - 1)

            if n == j and left and right:
                return True
            return False

        ans = helper(0, postorder_len - 1)
        return ans


if __name__ == '__main__':
    # postorder = [1, 6, 3, 2, 5]
    # postorder = [1, 3, 2, 6, 5]
    postorder = [4, 6, 7, 5]
    # postorder = [5, 2, -17, -11, 25, 76, 62, 98, 92, 61]
    ans = Solution().verifyPostorder(postorder)
    print(ans)
