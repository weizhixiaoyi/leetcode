# -*- coding:utf-8 -*-

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = list(filter(None, path))
        # print(path)
        ans = []
        for i in range(len(path)):
            if path[i] == '.':
                continue
            if path[i] == '..':
                if ans: ans.pop()
                continue
            ans.append(path[i])
        ans = '/'.join(ans)
        return '/' + ans


if __name__ == '__main__':
    # path = "/a/./b/../../c/"
    # path = "/a/../../b/../c//.//"
    # path = "/a//b////c/d//././/.."
    path = "/home//foo/"
    ans = Solution().simplifyPath(path)
    print(ans)
