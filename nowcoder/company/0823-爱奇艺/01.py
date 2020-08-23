# -*- coding:utf-8 -*-


def solve(a, b):
    a_list = a.split()
    a_list_len = len(a_list)
    b_list = b.strip().split()
    b_list_len = len(b_list)

    a_dict = {}
    for i in range(0, len(a) - 1):
        for j in range(i, len(a)):
            tmp1 = a[i: j + 1].replace(' ', '')
            tmp2 = a[i: j + 1].strip()
            a_dict[tmp1] = tmp2

    # 根据b中正确进行分段
    a_str = a.replace(' ', '')
    for i in range(b_list_len):
        if b_list[i] in a_str:
            a_str = a_str.replace(b_list[i], '#' + b_list[i] + '#')
    ans = a_str.split('#')

    for i in range(len(ans)):
        if ans[i] in a_dict:
            ans[i] = a_dict[ans[i]]
    return ' '.join(ans)


if __name__ == '__main__':
    a = input()
    b = input()

    # a = "aa bcd edf deda"
    # b = "ded"
    ans = solve(a, b)
    print(ans)
