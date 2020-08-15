# -*- coding:utf-8 -*-

def solve(nums, target):
    nums = sorted(nums, reverse=True)
    min_value = min(nums)
    if target < min_value: return -1

    def dfs(nums, target, path, ans):
        if ans[0] != float('inf'):
            return

        if target == 0:
            # print(path)
            ans[0] = min(ans[0], len(path))

        for num in nums:
            if target - num < 0: continue
            path.append(num)
            dfs(nums, target - num, path, ans)
            path.pop()

    ans = [float('inf')]
    dfs(nums, target, [], ans)
    if ans[0] == float('inf'):
        return -1
    else:
        return ans[0]


if __name__ == '__main__':
    # nums = [10, 20, 50]
    # target = 110
    nums = list(map(int, input().split()))
    target = int(input())
    ans = solve(nums, target)
    print(ans)
