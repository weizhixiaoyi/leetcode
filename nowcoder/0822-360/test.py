# -*- coding:utf-8 -*-


# types = [1, 2, 2, 2, 2]
# types = [str(v) for v in types]
# types_str = ''.join(types).replace('22', '')
# types = [v for v in types_str]
# print(types)

# from collections import deque
# q = [1, 2, 3, 4]
# print(q[4:] + q[:4])
"""
k = 0
while k < types_len - 1:
    if types[k] == 1:
        head = nums[0]
        nums = nums[1:] + [head]
        k += 1
    else:
        if types[k + 1] == 2:
            # 不需要改变
            k += 2
        else:
            for i in range(0, n, 2):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            k += 1
# 处理最后一个type
if types[-1] == 1:
    head = nums[0]
    nums = nums[1:] + [head]

return nums
"""

