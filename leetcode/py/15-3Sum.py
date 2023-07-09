class Solution:
    def threeSum(self, nums):
        res = []  # This will hold the result
        nums.sort()  # Sort the list in ascending order

        # Iterate through the list until the second last number
        for i in range(len(nums)-2):

            # If the current number is the same as the last, skip this iteration
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Set the left pointer to be the next number after i
            # Set the right pointer to be the last number in the list
            left, right = i+1, len(nums)-1

            # While the left pointer is less than the right pointer
            while left < right:
                # Calculate the sum of the current three numbers
                sum = nums[i] + nums[left] + nums[right]

                # If the sum is less than zero, we need it to be larger,
                # so we move the left pointer to the right
                if sum < 0:
                    left +=1 

                # If the sum is more than zero, we need it to be smaller,
                # so we move the right pointer to the left
                elif sum > 0:
                    right -= 1

                # If the sum is zero, we have a valid triplet
                else:
                    # We add the triplet to the result list
                    res.append((nums[i], nums[left], nums[right]))

                    # We move both pointers until the numbers they point to 
                    # are different from the numbers they were pointing to
                    # This is to avoid counting the same triplet multiple times
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # After dealing with duplicates, move both pointers 
                    # towards the center
                    left += 1
                    right -= 1

        # Return the result list
        return res
