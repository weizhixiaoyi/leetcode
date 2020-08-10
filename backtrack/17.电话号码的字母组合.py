from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_len = len(digits)
        if digits_len == 0: return []
        letter = 'abcdefghijklmnopqrstuvwxyz'
        from collections import defaultdict
        digit_letter_dict = defaultdict(str)
        k, digit = 0, 2
        while k < 26:
            if digit == 7 or digit == 9:
                digit_letter_dict[str(digit)] = letter[k: k + 4]
                digit += 1
                k += 4
            else:
                digit_letter_dict[str(digit)] = letter[k: k + 3]
                digit += 1
                k += 3

        from copy import deepcopy
        ans = []

        def helper(start, digits, path):
            if start == digits_len:
                ans.append(deepcopy(path))
                return

            for c in digit_letter_dict[digits[start]]:
                path += c
                helper(start + 1, digits, path)
                path = path[:-1]

        helper(0, digits, '')
        return ans


if __name__ == '__main__':
    digits = "23"
    # digits = ''
    ans = Solution().letterCombinations(digits)
    print(ans)
