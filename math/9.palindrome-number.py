# -*- coding:utf-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x1 = str(x)
        x2 = ''.join(list(reversed(str(x))))
        if x1 == x2:
            return True
        else:
            return False



if __name__ == '__main__':
    x = 122
    ans = Solution().isPalindrome(x)
    print('ans: ', ans)