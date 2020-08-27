# -*- coding:utf-8 -*-


def solve(width, height):
    width_len, height_len = len(width), len(height)
    min_width = min(width)
    max_width = max(width)
    min_height = min(height)
    max_height = max(height)
    if min_width <= 0 or min_height <= 0:
        return 0
    if max_width > 100 or max_height > 100:
        return 0
    if width_len != height_len:
        return 0
    if width_len <= 0 or width_len > 100:
        return 0

    # print(width)
    # print(height)
    max_ans = 0
    for i in range(height_len):
        cur_ans = height[i] * width[i]
        cur_height = height[i]
        k = i - 1
        while k >= 0 and height[k] >= cur_height:
            cur_ans += width[k] * cur_height
            k -= 1
        k = i + 1
        while k < height_len and height[k] >= cur_height:
            cur_ans += width[k] * cur_height
            k += 1
        max_ans = max(max_ans, cur_ans)
    return max_ans


if __name__ == '__main__':
    line = input()
    width, height = line.split('],[')
    width = width.replace('[', '')
    height = height.replace(']', '')
    width = width.split(',')
    height = height.split(',')
    width = [int(val) for val in width]
    height = [int(val) for val in height]
    ans = solve(width, height)
    print(ans)
