class Solution:
    def check(self, word, row):
        for w in set(word):
            if w not in row:
                return False
        return True
    
    def findWords(self, words):
        first = set("qwertyuiopQWERTYUIOP")
        second = set("asdfghjklASDFGHJKL")
        third = set("zxcvbnmZXCVBNM")
        ans = []
        for w in words:
            if self.check(w, first) or self.check(w, second) or self.check(w, third):
                ans.append(w)  
        return ans