# -*- coding:utf-8 -*-

def solve(n, nums):
    odd, even = 0, 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0 or even == 0:
        return nums
    elif odd == even:
        nums = sorted(nums)
        return nums
    else:
        # min_value = min(odd, even)
        # nums_sorted = sorted(nums)
        # ans1 = nums_sorted[:min_value]
        # ans3 = nums_sorted[-min_value:]
        # ans2 = []
        # for num in nums:
        #     if (num in ans1) or (num in ans3):
        #         continue
        #     ans2.append(num)
        # return ans1 + ans2 + ans3
        return sorted(nums)


if __name__ == '__main__':
    # n = 10
    # nums = [53941, 38641, 31525, 75864, 29026, 12199, 83522, 58200, 64784, 80987]
    # n = 4
    # nums = [7, 5, 3, 2]
    n = int(input())
    nums = list(map(int, input().split()))
    ans = solve(n, nums)
    ans = [str(v) for v in ans]
    ans = ' '.join(ans)
    print(ans)
