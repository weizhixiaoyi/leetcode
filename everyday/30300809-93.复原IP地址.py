# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def helper(cur_s, ip):
            # 截止条件
            ip_str = ''.join(ip)
            if ip_str == s and len(ip) == 4:
                ans.append('.'.join(ip))

            # 操作
            for k in range(1, min(4, len(cur_s) + 1)):
                # 剪枝
                if int(cur_s[:k]) > 255: continue
                if len(cur_s[:k]) == 2 and int(cur_s[:k]) < 10: continue
                if len(cur_s[:k]) == 3 and int(cur_s[:k]) < 100: continue
                if len(ip) >= 4: continue
                # 回溯
                ip.append(cur_s[:k])
                helper(cur_s[k:], ip)
                ip.pop()

        helper(s, [])
        return ans


if __name__ == '__main__':
    # s = "25525511135"
    # s = '0000'
    s = "010010"
    ans = Solution().restoreIpAddresses(s)
    print(ans)
