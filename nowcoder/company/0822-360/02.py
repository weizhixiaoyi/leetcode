# -*- coding:utf-8 -*-


def solve(n, types, types_len):
    nums = [i + 1 for i in range(n)]

    # 处理22
    types_str = ''.join(types).replace('22', '')
    types = [int(v) for v in types_str]
    types_len = len(types)

    # 处理连续的1
    new_types = []
    k, lian = 0, 0
    while k < types_len:
        if types[k] == 1:
            lian += 1
            k += 1
            continue
        else:
            lian = lian % n
            if lian == 0: continue
            new_types.append(lian)
            lian = 0
            new_types.append(-1)
            k += 1
    # print(lian)
    if lian:
        new_types.append(lian)

    types = new_types
    types_len = len(types)
    for k in range(0, types_len):
        if types[k] == -1:
            for i in range(0, n, 2):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            cur = types[k]
            nums = nums[cur:] + nums[:cur]
    return nums


if __name__ == '__main__':
    n, m = map(int, input().split())
    types = input().split()
    ans = solve(n, types, m)
    ans = [str(v) for v in ans]
    print(' '.join(ans))
