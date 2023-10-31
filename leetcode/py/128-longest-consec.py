from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Early return cases
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        # Convert list to a set for O(1) lookups
        num_set = set(nums)

        maxLength = 0  # Variable to keep track of the maximum sequence length

        # Loop through each number in the original list
        for num in nums:
            # Check if num is the starting point of a sequence
            if num - 1 not in num_set:
                # This means we can start counting from this number
                current_num = num
                current_streak = 1  # Initialize current streak to 1
                
                # Start looking for the next number in the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update maxLength if we found a longer streak
                maxLength = max(maxLength, current_streak)

        return maxLength

# Example usage
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output should be 4
