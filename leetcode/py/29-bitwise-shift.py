class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge Case: The mathematical result would be 2**31,
        # but the problem specifies a 32-bit signed integer, which has a maximum value of 2**31 - 1.
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Calculate sign of the result
        # XOR (^) will be true if one of them is negative (and not both)
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

        # Use absolute values to make calculations easier
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0  # Initialize quotient to 0, which will store the final answer

        # Outer loop runs as long as the dividend is greater than or equal to the divisor
        while dividend >= divisor:
            temp = divisor  # Start 'temp' at divisor
            multiple = 1    # Initialize 'multiple' at 1
            
            # Inner loop aims to make 'temp' the largest value that is still smaller than or equal to 'dividend'
            while dividend >= temp + temp:
                temp += temp  # Double 'temp'
                multiple += multiple  # Double 'multiple'

            # Subtract the 'temp' value from 'dividend'
            dividend -= temp

            # Add the 'multiple' to the 'quotient'
            quotient += multiple

        # Apply the previously calculated 'sign' to the 'quotient'
        # And keep it within 32-bit signed integer bounds
        return min(max(-2**31, quotient * sign), 2**31 - 1)

# Example usage
solution = Solution()

# Example 1: 10 divided by 3 equals 3 with a remainder of 1
print(solution.divide(10, 3))  # Output should be 3

# Example 2: -10 divided by 3 equals -3 with a remainder of 1
print(solution.divide(-10, 3))  # Output should be -3

# Example 3: -10 divided by -3 equals 3 with a remainder of 1
print(solution.divide(-10, -3))  # Output should be 3
