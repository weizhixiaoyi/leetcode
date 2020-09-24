# -*- coding:utf-8 -*-

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.ans = []

        used = [False for i in range(101)]
        from queue import Queue
        q = Queue()
        q.put(node)

        ans = [Node(i) for i in range(101)]
        while not q.empty():
            cur = q.get()
            if used[cur.val]: continue
            used[cur.val] = True

            for neighbor in cur.neighbors:
                q.put(neighbor)

                neighbor_node = ans[neighbor.val]
                ans[cur.val].neighbors.append(neighbor_node)

        return ans[1]
