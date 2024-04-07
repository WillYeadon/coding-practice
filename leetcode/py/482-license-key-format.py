class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(char for char in s if char.isalnum())
        s = s.upper()[::-1]
        ans = ''
        while len(s) >= k:
            ans += s[:k]
            ans += '-'
            s = s[k:]
        if len(s) > 0:
            ans += s
        else:
            ans = ans[:-1]
        
        return ans[::-1]