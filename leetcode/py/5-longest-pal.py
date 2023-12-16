class Solution:
    # checks we're pals outwards
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        # 0 and 1 are pals
        if len(s) < 2:
            return s

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            odd_pal = self.expandAroundCenter(s, i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal

            # Even length palindromes
            even_pal = self.expandAroundCenter(s, i, i + 1)
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest
