class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s) # Length of the input string
        wordSet = set(wordDict) # Convert the word dictionary into a set for faster lookup
        
        # Initialize a dynamic programming (DP) array of size n + 1 with False
        # dp[i] will be True if the substring s[:i] can be segmented into words in wordDict
        dp = [False] * (n + 1)
        
        # Base case: an empty string can always be segmented, so we set dp[0] to True
        dp[0] = True

        # Outer loop to iterate over the entire string s
        for i in range(1, n + 1):
            
            # Inner loop to iterate from 0 to i
            # We are trying to find a j that breaks s[:i] into two parts: s[:j] and s[j:i]
            # where s[:j] has a valid segmentation (dp[j] is True), and s[j:i] is a word in wordDict
            for j in range(i):
                
                # Check if s[:j] has a valid segmentation (dp[j] is True)
                # And if s[j:i] is a word in wordDict (s[j:i] is in wordSet)
                if dp[j] and s[j:i] in wordSet:
                    
                    # If both conditions are met, s[:i] has a valid segmentation
                    # So we set dp[i] to True and break out of the inner loop
                    dp[i] = True
                    break

        # The final result is dp[n], which tells us if the entire string s can be segmented
        return dp[n]
