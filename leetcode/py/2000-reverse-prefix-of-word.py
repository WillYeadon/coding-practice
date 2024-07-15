class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            pos = word.index(ch) + 1
            a = word[0:pos]
            b = word[pos:]
            return a[::-1] + b
        return word