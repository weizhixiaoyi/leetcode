# -*- coding:utf-8 -*-

a, b = input().split()
a_len, b_len = len(a), len(b)


# print(a, b)

# a, b = '72106547548473106236', '982161082972751393'
# a, b = '12', '45'
# a_len, b_len = len(a), len(b)
# print(int(a) * int(b))


def multi_one(a, b_value, index):
    b_value = int(b_value)
    # print(a, b_value)
    # print(int(a) * b_value)

    temp_ans = ''
    pre = 0
    for k in range(a_len - 1, -1, -1):
        cur_a_value = int(a[k])
        temp_val = cur_a_value * b_value + pre
        # print(temp_val)
        temp_val = str(temp_val)
        if len(temp_val) == 1:
            temp_ans = temp_val + temp_ans
            pre = 0
        else:
            temp_ans = temp_val[1] + temp_ans
            pre = int(temp_val[0])
            # print(pre)
        # print(temp_ans)
        # print('*' * 10)
    if pre != 0:
        temp_ans = str(pre) + temp_ans
    temp_ans += '0' * (b_len - index - 1)
    if '0' * len(temp_ans) == temp_ans:
        temp_ans = '0'

    return temp_ans


multi = []
for k in range(b_len - 1, -1, -1):
    cur_b_value = b[k]
    cur_multi = multi_one(a, cur_b_value, k)
    # print(cur_multi)
    multi.append(cur_multi)


def add_one(a_value, b_value):
    # print(a_value, b_value)
    if b_value == '0':
        return a_value

    a_value_len, b_value_len = len(a_value), len(b_value)
    i, j = a_value_len - 1, b_value_len - 1
    temp_ans = ''
    pre = 0
    while i >= 0 and j >= 0:
        temp_value = int(a_value[i]) + int(b_value[j]) + pre
        temp_value = str(temp_value)
        if len(temp_value) == 1:
            temp_ans = temp_value + temp_ans
            pre = 0
        else:
            temp_ans = temp_value[1] + temp_ans
            pre = int(temp_value[0])

        i -= 1
        j -= 1

    while i >= 0:
        temp_value = int(a_value[i]) + pre
        temp_value = str(temp_value)
        if len(temp_value) == 1:
            temp_ans = temp_value + temp_ans
            pre = 0
        else:
            temp_ans = temp_value[1] + temp_ans
            pre = int(temp_value[0])
        i -= 1

    while j >= 0:
        temp_value = int(b_value[j]) + pre
        temp_value = str(temp_value)
        if len(temp_value) == 1:
            temp_ans = temp_value + temp_ans
            pre = 0
        else:
            temp_ans = temp_value[1] + temp_ans
            pre = int(temp_value[0])
        j -= 1
    if pre != 0:
        temp_ans = str(pre) + temp_ans

    real_value = int(a_value) + int(b_value)
    # print(real_value)
    # print(temp_ans)
    # print('#' * 10)
    return temp_ans


multi_len = len(multi)
ans = '0'
real_ans = '0'
for k in range(0, multi_len):
    ans = add_one(ans, multi[k])
print(ans)
