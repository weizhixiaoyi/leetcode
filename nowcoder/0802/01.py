# -*- coding:utf-8 -*-

kn = list(map(int, input().split()))
k, n = kn[0], kn[1]
nums = list(map(int, input().split()))

# k, n = 6, 3
# nums = [4, 2, 6]
# k, n = 10, 4
# nums = [6, 3, 3, 3]

flag = False
pre = 0
value = 0
for i in range(n):
    cur_dis = k - value
    value += nums[i]
    if value == k:
        flag = True

    # not equal
    if value > k:
        # print(value, cur_dis)
        value = (k - (nums[i] - cur_dis))
        pre += 1

# k == 0的时候也是要进行输出paradox
if k == 0 or flag is True:
    print("paradox")
elif pre == 0:
    print(k - value, 0)
else:
    print(k - value, pre)
