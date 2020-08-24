# -*- coding:utf-8 -*-

def solve(n, points, points_len):
    from collections import defaultdict
    nums_dict = defaultdict(list)
    for i in range(points_len):
        a, b = points[i]
        nums_dict[a].append(b)
        nums_dict[b].append(a)

    # print(nums_dict)
    ans = 0
    for i in range(1, n + 1):
        cur_ans = 1
        gx = nums_dict[i]
        for j in range(1, n + 1):
            if i == j:
                continue
            gy = nums_dict[j]
            if gx == gy:
                cur_ans += 1
        ans = max(cur_ans, ans)

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    points = []
    for i in range(m):
        a, b = map(int, input().split())
        points.append([a, b])
    ans = solve(n, points, m)
    print(ans)
