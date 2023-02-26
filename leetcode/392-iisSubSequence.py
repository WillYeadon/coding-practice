class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
            
        counts = {}
        countt = {}
        for i in s:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        for i in t:
            if i not in countt:
                countt[i] = 1
            else:
                countt[i] += 1

        for i in counts:
            if counts[i] > countt[i]:
                return False

        flag = True

        for i in s:
            if i in t:
                index = t.index(i)
                t = t[index:]
            else:
                flag = False

        if flag:
            return True
        else:
            return False
        
x = Solution()
print(x.isSubsequence('leeeeetcode', 'yyyyyyylyyyyyyyeeeeeeteetttccoooddee')) 
print(x.isSubsequence('aaaaaa', 'bbaaaa'))       