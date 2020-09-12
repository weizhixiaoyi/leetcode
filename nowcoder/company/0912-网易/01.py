# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, node_dict):
        node_list = [TreeNode(0)]
        for i in range(1, m + 1):
            node_list.append(TreeNode(i))
        for i in range(1, m + 1):
            cur_node = node_list[i]
            left = node_dict[i]['left']
            right = node_dict[i]['right']
            if left != 0:
                cur_node.left = node_list[left]
            if right != 0:
                cur_node.right = node_list[right]
        return node_list[1]

    def solve(self, root):
        self.ans = 0

        def dfs(root):
            if root is None: return None

            dfs(root.left)
            if root.left and root.right:
                if (not root.left.left and not root.left.right) and (not root.right.left and not root.right.left):
                    self.ans += 1
            dfs(root.right)

        dfs(root)
        return self.ans


if __name__ == '__main__':
    m, n = map(int, input().split())
    node_dict = {i: {'left': 0, 'right': 0} for i in range(1, m + 1)}
    for i in range(n):
        line = input().split()
        a, type, b = int(line[0]), line[1], int(line[2])
        if type == 'left':
            node_dict[a]['left'] = b
        if type == 'right':
            node_dict[a]['right'] = b
    root = Solution.buildTree(m, node_dict)
    ans = Solution().solve(root)
    print(ans)
