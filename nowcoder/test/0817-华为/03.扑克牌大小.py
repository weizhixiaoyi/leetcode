# -*- coding:utf-8 -*-

def cmp(c1, c2):
    c1.replace('J', '11')
    c2.replace('J', '11')
    c1.replace('Q', '12')
    c2.replace('Q', '12')
    c1.replace('K', '13')
    c2.replace('K', '13')
    c1.replace('A', '14')
    c2.replace('A', '14')
    c1.replace('2', '15')
    c2.replace('2', '15')
    c1.replace('joker', '16')
    c2.replace('joker', '16')
    c1.replace('JOKER', '17')
    c2.replace('JOKER', '17')

    if int(c1) > int(c2):
        return True
    else:
        return False


def solve(a, b):
    a_list, b_list = a.split(), b.split()
    a_list_len, b_list_len = len(a_list), len(b_list)
    # 谁有炸弹和对子谁赢
    if 'joker JOKER' in a:
        return a
    if 'joker JOKER' in b:
        return b
    if a_list_len == 4 and b_list_len != 4:
        return a
    if a_list_len != 4 and b_list_len == 4:
        return b

    # 单张牌; 对子; 顺子; 只需要比较最小的牌
    if a_list_len == b_list_len:
        if cmp(a_list[0], b_list[0]):
            return a
        else:
            return b

    return "ERROR"


if __name__ == '__main__':
    line = input().split('-')
    a, b = line[0], line[1]
    ans = solve(a, b)
    print(ans)
