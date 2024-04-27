class Solution:
    def find_all_substrings(self, s):
        substrings = []
        length = len(s)
        for start in range(length):
            for end in range(start + 1, length + 1):
                substrings.append(s[start:end])
        return substrings
    def test(self, a, b):
        return not (a in b)
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        substrings = self.find_all_substrings(longer)
        longest = -1
        for s in substrings:
            if self.test(s, shorter):
                longest = max(longest, len(s))
        return longest