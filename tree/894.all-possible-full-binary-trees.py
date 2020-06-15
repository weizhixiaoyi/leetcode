# -*- coding:utf-8 -*-

from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 针对递归问题, 不需要理解构建的具体细节过程, 只需要清楚函数的返回值和构建过程
# 重点
# 1. 递归函数的作用(以N构建满二叉树) 输入: N, 输出: 满二叉树
# 2. 递归的截止条件 N == 1时只返回当前节点即可, N % 2 == 0不可构建满二叉树
# 3. 递归构建过程
#    针对返回的左子树和右子树, 只需遍历利用root关联起来即可.

class Solution:
    import functools
    @functools.lru_cache(None)
    def allPossibleFBT(self, N: int):
        res = []
        # 递归截止条件
        # 如果只有一个节点, 那么把当前节点当作root, 返回该节点
        if N == 1: return [TreeNode(0)]
        # 如果是偶数个节点, 则不再可能递归的构建子树
        if N % 2 == 0: return []

        # 因为是满二叉树, 左边节点最多N-2个节点, 因为root和右子树需要占用一个节点
        for k in range(1, N - 2 + 1):
            # 以k个节点构建的左子树, 满二叉树
            left_tree = self.allPossibleFBT(k)
            # 以n - 1 - k个节点构建的右子树, 同样也是满二叉树
            right_tree = self.allPossibleFBT(N - 1 - k)

            # 根据构建的左子树和右子树, 利用root进行关联起来, 形成满二叉树
            for i in range(len(left_tree)):
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)
        return res


if __name__ == '__main__':
    n = 7
    ans = Solution().allPossibleFBT(n)
