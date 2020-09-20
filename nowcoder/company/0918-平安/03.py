# -*- coding:utf-8 -*-


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param actions string字符串一维数组
# @return int整型一维数组
#
class Solution:
    def count(self, actions):
        ans = []
        from collections import defaultdict
        str_dict = defaultdict(int)
        for action in actions:
            q, s = action.split()
            if q == 'I':
                str_dict[s] += 1
            if q == 'Q':
                if s in str_dict:
                    ans.append(str_dict[s])
                else:
                    ans.append(0)
        return ans

if __name__ == '__main__':
    line = input().replace('[', '').replace(']', '').replace('\"', '')
    line = line.split(',')
    ans = Solution().count(line)
    print(ans)
