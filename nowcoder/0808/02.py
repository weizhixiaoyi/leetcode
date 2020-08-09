# -*- coding:utf-8 -*-

def solve(a_nums, b_nums):
    a_nums_len, b_nums_len = len(a_nums), len(b_nums)

    dp = [0 for i in range(a_nums_len)]
    for i in range(0, a_nums_len):
        if i == 0:
            dp[0] = a_nums[0]
        else:
            dp[i] = min(dp[i - 1] + a_nums[i], dp[i - 2] + b_nums[i - 1])

    min_value = dp[a_nums_len - 1]
    hour = min_value // 3600
    minuters = (min_value - hour * 3600) // 60
    seconds = (min_value - hour * 3600 - minuters * 60)
    hour = hour + 8
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    if minuters < 10:
        minuters = "0" + str(minuters)
    else:
        minuters = str(minuters)
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    time_str = hour + ":" + minuters + ":" + seconds

    if int(hour) <= 12:
        return time_str + " am"
    else:
        return time_str + " pm"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if n == 1:
            val = input()
            if int(val) < 10: val = "0" + val
            print('08:00:' + val + ' am')
        else:
            a = list(map(int, input().split()))
            b = list(map(int, input().split()))
            ans = solve(a, b)
            print(ans)
