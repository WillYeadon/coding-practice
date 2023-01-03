# Explain what the following code does ((n & (n - 1)) == 0)

# Here & means 1 & 1 = 1 whilst rest (1&0, 0&1, 1&1) = 0

# == 0 checks for if the same as 00000000, depending on
# your definition of 1 as 11111111 or 00000001 will give
# whether it tests for whether even or odd of whether it
# tests for 0 bit content / whether there are matching
# 1s (rest either 10/01/00) -> ans says this thus
# follows it tests for powers of 2. 