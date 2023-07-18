from typing import List

class Solution:
    mapping = {
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def recursive(self, digits, combination, result):
        if len(digits) == 0:
            result.append(combination)
            return
        for c in self.mapping[digits[0]]:
            self.recursive(digits[1:], combination + c, result)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        self.recursive(digits, '', result)
        return result
