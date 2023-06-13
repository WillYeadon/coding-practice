from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def createDict(x):
            ans = {}
            if not x:
                return ans

            for i in x:
                if i not in ans:
                    ans[i] = 1
                else:
                    ans[i] += 1
            return ans
        
        def isAna(x, y):
            for key in x:
                if x[key] != y[key]:
                    return False
            
            return True

        ana = createDict(p)
        win = len(p)
        overall = len(s)
        indexes = []

        if (win < 1) or (overall < 1):
            return indexes

        for i, v in enumerate(s):
            end = i + win
            if end - 1 < overall:
                if isAna(createDict(s[i:end]), ana):
                    print(createDict(s[i:end]), ana)
                    indexes.append(i)              

        return indexes 
    
x = Solution()
print(x.findAnagrams("ababababab", "aab"))