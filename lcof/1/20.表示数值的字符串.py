# -*- coding:utf-8 -*-

class Solution:
    def isNumber(self, s: str) -> bool:
        # 去除头尾的空格;如果中间还存在字符的话, 则为False
        s = s.strip(' ')
        if not s: return False
        if ' ' in s: return False

        # 如果包含除e以外的字母, 则为False
        for c in s:
            if c.isalpha() and c != 'e':
                return False

        e_count = s.count('e')
        dot_count = s.count('.')
        # 如果e和.的个数大于1则为False
        if e_count > 1 or dot_count > 1:
            return False

        # A.B[e]C, 只有A和C开始位置可以带符号, 其他位置不能再有符号
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if e_count == 0:
            if '+' in s or '-' in s:
                return False

            # s不能只为.
            if dot_count == 1 and len(s) == 1:
                return False
            return True

        if e_count == 1:
            s = s.replace('e+', 'e')
            s = s.replace('e-', 'e')
            if '+' in s or '-' in s:
                return False

            if dot_count == 0:
                if len(s) == 1: return False
                e1, e2 = s.split('e')
                if e1 == '' or e2 == '':
                    return False
                return True

            if dot_count == 1:
                if len(s) == 2: return False
                e1, e2 = s.split('e')
                if e1 == '' or e2 == '':
                    return False
                if '.' in e2:
                    return False

                if len(e1) == 1: return False
                return True
            return True


if __name__ == '__main__':
    s = " 3.1416 "
    ans = Solution().isNumber(s)
    print(ans)
