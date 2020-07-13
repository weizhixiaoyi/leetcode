# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], poped: List[int]) -> bool:
        push_len = len(pushed)
        k = 0
        help_stack = []

        while True:
            if k < push_len:
                help_stack.append(pushed[k])
                k += 1
            # print(help_stack)

            while len(poped) > 0 and len(help_stack) > 0 and help_stack[-1] == poped[0]:
                help_stack.pop()
                poped = poped[1:]
            # print(help_stack)
            if len(help_stack) == 0 and len(poped) == 0:
                return True

            if k == push_len and len(poped) != 0:
                return False


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    # poped = [4, 5, 3, 2, 1]
    poped = [4, 3, 5, 1, 2]
    # pushed = [4, 0, 1, 2, 3]
    # poped = [4, 2, 3, 0, 1]
    ans = Solution().validateStackSequences(pushed, poped)
    print(ans)

# push_len = len(pushed)
# pop_len = len(poped)
# if push_len != pop_len: return False
#
# push_set = set(pushed)
# pop_set = set(poped)
# if push_set != pop_set: return False
#
# if push_len == 0: return True
# if push_len == 1: return True
# if push_len == 2: return True
#
# ans = [poped[0]]
# min_value = ans[0]
# max_value = ans[0]
# for i in range(1, pop_len):
#     if poped[i] < min_value:
#         min_value = poped[i]
#         ans.insert(0, poped[i])
#     if poped[i] > max_value:
#         max_value = poped[i]
#         ans.append(poped[i])
#
# return ans == pushed
