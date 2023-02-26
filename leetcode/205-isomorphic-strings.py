# Checking if two strings are isomorphic
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Early exit check to see if same length
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        # Loop through the strings
        for i in range(len(s)):
            # If already added to dictionary S check whether if
            # in dictionary T. If not then the letters were not
            # the same
            if s[i] in s_map:
                if s_map[s[i]] != t[i]:
                    return False
            else:
                # If s is not in s_map it should also not be in
                # t_map, check fot his
                if t[i] in t_map:
                    return False
                
                # Will make the dictionary key s[i] have value t[i] 
                # whereas key t[i] have value s[i]. Thus for a, b
                # will give {b : a} for s and {a : b} for t.
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]       
        
        return True
    
x = Solution()
print(x.isIsomorphic("bbbaaaba","aaabbbba"))
print(x.isIsomorphic("paper","title"))
