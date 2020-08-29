# -*- coding:utf-8 -*-


if __name__ == '__main__':
    m = int(input().strip())
    idx = 0
    values = []
    for i in range(m):
        line = list(map(int, input().strip().split()))
        values.append(line)

    nums = []
    for i in range(m):
        line = values[i]
        op = line[0]
        if op == 1:
            a, b = line[1], line[2]
            a -= 1
            nums.insert(a, str(b))
        if op == 2:
            a = line[1]
            a -= 1
            nums.pop(a)
        if op == 3:
            print(' '.join(nums))
