# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 模拟
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        if l == 1 and gas[0] >= cost[0]: return 0
        if l == 1 and gas[0] < cost[0]: return -1

        for i in range(0, l):
            # 可以从第k个点出发
            if gas[i] >= cost[i]:
                flag = True
                temp_gas = gas[i:] + gas[0:i]
                temp_cost = cost[i:] + cost[0:i]
                # print(temp_gas)
                # print(temp_cost)
                k = 1
                temp_gas_sum, temp_cost_sum = 0, 0
                while k <= l:
                    temp_gas_sum += temp_gas[k - 1]
                    temp_cost_sum += temp_cost[k - 1]
                    # temp_gas_sum = sum(temp_gas[0:k])
                    # temp_cost_sum = sum(temp_cost[0:k])
                    # print(temp_gas_sum, temp_cost_sum)
                    if temp_gas_sum >= temp_cost_sum:
                        k += 1
                    else:
                        flag = False
                        break
                if flag is True:
                    return i
        return -1
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        if l == 1 and gas[0] >= cost[0]: return 0
        if l == 1 and gas[0] < cost[0]: return -1

        start = 0
        total, cur = 0, 0
        for i in range(0, l):
            total += (gas[i] - cost[i])
            cur += (gas[i] - cost[i])

            # 如果从A到B的油量不够, 那么从其他位置出发位置也是不够的
            if cur < 0:
                cur = 0
                start = i + 1
        if total < 0 or cur < 0:
            return -1
        return start


if __name__ == '__main__':
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    ans = Solution().canCompleteCircuit(gas, cost)
    print(ans)
