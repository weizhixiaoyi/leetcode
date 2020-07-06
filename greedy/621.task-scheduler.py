# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_len = len(tasks)
        if tasks_len <= 1: return tasks_len

        task_dict = {}
        for task in tasks:
            task_dict[task] = task_dict.get(task, 0) + 1
        task_sort = sorted(task_dict.items(), key=lambda d: d[1], reverse=True)

        max_task_count = int(task_sort[0][1])
        ans = (max_task_count - 1) * (n + 1)
        for v in task_sort:
            if v[1] == max_task_count:
                ans += 1

        return ans if tasks_len < ans else tasks_len


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"]
    n = 2
    ans = Solution().leastInterval(tasks, n)
    print(ans)
