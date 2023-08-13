class Solution:
    def reverseWords(self, s: str) -> str:        
        split = s.split(' ')
        split = [item for item in split if item != '']
        ans = ''
        if len(split) == 1:
            return split[0]
        else:
            for i in range(len(split) - 1, 0, -1):
                ans += split[i]
                ans += ' '
            ans += split[0]
            return ans
        