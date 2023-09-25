class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Quick length check: the sum of lengths of s1 and s2 must be equal to the length of s3
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize a DP table. 
        # dp[i][j] will be True if s3[:i+j] is an interleaving of s1[:i] and s2[:j].
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # Base case: both s1 and s2 are empty strings, so s3 must also be an empty string.
        dp[0][0] = True
        
        # Loop through all the subproblems we need to solve.
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                
                # If i > 0, it means we can consider characters from s1.
                if i > 0:
                    # Update dp[i][j] based on the previous row (i-1).
                    # Only set it to True if both dp[i-1][j] is True and the current character in s3 matches the current character in s1.
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
                
                # If j > 0, it means we can consider characters from s2.
                if j > 0:
                    # Update dp[i][j] based on the previous column (j-1).
                    # Only set it to True if both dp[i][j-1] is True and the current character in s3 matches the current character in s2.
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        # The last cell in the DP table gives us the answer to the original problem.
        return dp[-1][-1]
